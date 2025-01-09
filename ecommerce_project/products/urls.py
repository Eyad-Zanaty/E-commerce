from django.urls import path
from .views import home, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('', home, name='home'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
