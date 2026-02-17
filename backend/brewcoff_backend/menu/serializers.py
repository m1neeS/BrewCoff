from rest_framework import serializers
from .models import Category, MenuItem, Modifier

# Serializer untuk Modifier
class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ['id', 'modifier_type', 'option_name', 'price_adjustment']

# Serializer untuk MenuItem(dengan modifiers)
class MenuItemSerializer(serializers.ModelSerializer):
    modifiers = ModifierSerializer(many=True, read_only=True) # include modifiers
    category_name = serializers.CharField(source='category.name', read_only=True) # nama kategori

    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'base_price', 'image', 'is_available',
            'category', 'category_name', 'modifiers', 'created_at'
        ]

# Serializer untuk category
class CategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'items']
