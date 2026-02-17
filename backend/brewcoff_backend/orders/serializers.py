from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import MenuItemSerializer

# Serializer untuk OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_detail = MenuItemSerializer(source='menu_item', read_only=True)  # Detail menu
    
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_detail', 'quantity', 'selected_modifiers', 'subtotal']

# Serializer untuk create OrderItem (tanpa detail menu)
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity', 'selected_modifiers', 'subtotal']

# Serializer untuk Order
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Include order items
    
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'table_number', 'status', 'total_price', 
                  'created_at', 'updated_at', 'items']
        read_only_fields = ['created_at', 'updated_at']

# Serializer untuk create Order (dengan items)
class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)  # Accept items saat create order
    
    class Meta:
        model = Order
        fields = ['customer_name', 'table_number', 'total_price', 'items']
    
    def create(self, validated_data):
        # Ambil items dari data
        items_data = validated_data.pop('items')
        # Buat order dulu
        order = Order.objects.create(**validated_data)
        # Buat order items
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
