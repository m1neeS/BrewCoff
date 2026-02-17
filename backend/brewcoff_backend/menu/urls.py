from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet

# Router untuk auto-generate URLs
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]
