from django.contrib import admin
from .models import Order, OrderItem

# Register models ke admin panel
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'table_number', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at']  # Filter berdasarkan status dan waktu
    search_fields = ['customer_name', 'table_number']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity', 'subtotal']
    list_filter = ['menu_item']
