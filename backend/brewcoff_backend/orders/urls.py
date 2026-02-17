from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

# Router untuk auto-generate URLs
router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
