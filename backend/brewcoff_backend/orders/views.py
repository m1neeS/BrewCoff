from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer

# ViewSet untuk Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        # Pakai serializer berbeda untuk create
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    # Custom action untuk update status order
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')
        
        # Validasi status
        valid_statuses = ['pending', 'preparing', 'ready', 'completed']
        if new_status not in valid_statuses:
            return Response({'error': 'Invalid status'}, status=400)
        
        order.status = new_status
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    # Custom action untuk get orders by table
    @action(detail=False, methods=['get'])
    def by_table(self, request):
        table_number = request.query_params.get('table_number')
        if table_number:
            orders = self.queryset.filter(table_number=table_number).order_by('-created_at')
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        return Response({'error': 'table_number required'}, status=400)