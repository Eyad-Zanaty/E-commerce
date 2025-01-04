from django.urls import path
from .views import manage_products, product_detail

urlpatterns = [
    path('products/', manage_products, name='manage_products'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]