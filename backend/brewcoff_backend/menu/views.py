from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer

# ViewSet untuk Category
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ViewSet untuk MenuItem
class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.filter(is_available=True)  # Hanya yang available
    serializer_class = MenuItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']  # Bisa search berdasarkan nama dan deskripsi

    # Custom action untuk filter by category
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get("category_id")
        if category_id:
            items = self.queryset.filter(category_id=category_id)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        return Response({'error': 'category_id required'}, status=400)