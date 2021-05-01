from django.urls import path
from webapp.views import (
    IndexProducts,
    ProductView, ProductCreate, ProductUpdate,
)

app_name = 'products'

urlpatterns = [
    path('', IndexProducts.as_view(), name='index_products'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
]
