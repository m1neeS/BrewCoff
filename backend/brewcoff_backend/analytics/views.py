from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from orders.models import Order, OrderItem
from  menu.models import MenuItem, Category

@api_view(['GET'])
def dashboard_summary(request):
    """
    Summary dashboard: total sales, orders, dll
    """

    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)

    # total sales
    total_sales_today = Order.objects.filter(
        created_at__date=today
    ).aggregate(total=Sum('total_price'))['total'] or 0

    total_sales_week = Order.objects.filter(
        created_at__date__gte= week_ago
    ).aggregate(total=Sum('total_price'))['total'] or 0

    total_sales_month = Order.objects.filter(
        created_at__date__gte=month_ago
    ).aggregate(total=Sum('total_price'))['total'] or 0


    # total orders by status
    orders_by_status = Order.objects.values('status').annotate(count=Count('id'))

    # total orders today
    orders_today = Order.objects.filter(created_at__date=today).count()

    return Response({
        'sales':{
            'today': float(total_sales_today),
            'week': float(total_sales_week),
            'month': float(total_sales_month),
        },
        'orders':{
            'today': orders_today,
            'by_status': list(orders_by_status),
        }
    })

@api_view(['GET'])
def popular_items(request):
    """
    Menu items terpopuler berdasarkan jumlah order
    """
    limit = int(request.query_params.get('limit', 10))

    popular = OrderItem.objects.values(
        'menu_item__id',
        'menu_item__name',
        'menu_item__base_price'
    ).annotate(
        total_ordered = Sum('quantity'),
        total_revenue = Sum('subtotal')
    ).order_by('-total_ordered')[:limit]

    return Response(list(popular))

@api_view(['GET'])
def revenue_by_category(request):
    """
    Revenue per kategori menu
    """
    categories = Category.objects.all()
    result = []

    for category in categories:
        revenue = OrderItem.objects.filter(
            menu_item__category = category
        ).aggregate(total=Sum('subtotal'))['total'] or 0

        result.append({
            'category_id': category.id,
            'category_name': category.name,
            'revenue': float(revenue)
        })

    return Response(result)

@api_view(['GET'])
def order_trends(request):
    """
    Trend orders per hari(7 hari terakhir)
    """
    today = timezone.now().date()
    trends = []

    for i in range(7):
        date = today - timedelta(days=i)
        orders_count = Order.objects.filter(created_at__date=date).count()
        revenue = Order.objects.filter(
            created_at__date =date
        ).aggregate(total=Sum('total_price'))['total'] or 0

        trends.append({
            'date': str(date),
            'orders': orders_count,
            'revenue': float(revenue)
        })

    return Response(trends)