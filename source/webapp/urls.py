from django.urls import path
from webapp.views import (
    IndexProducts,
    ProductView, ProductCreate,
)

app_name = 'products'

urlpatterns = [
    path('', IndexProducts.as_view(), name='index_products'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreate.as_view(), name='product_add'),
]
