from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.dashboard_summary, name='dashboard-summary'),
    path('popular-items/', views.popular_items, name='popular-items'),
    path('revenue-by-category/', views.revenue_by_category, name='revenue-by-category'),
    path('order-trends/', views.order_trends, name='order-trends'),
]
