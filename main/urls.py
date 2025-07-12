from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>/update/', ProductEditView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('customer/', CustomerView.as_view(), name='customer'),
]