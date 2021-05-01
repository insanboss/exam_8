from django.urls import path
from webapp.views import (
    IndexProducts,
    ProductView, ProductCreate, ProductUpdate, ProductDelete,
)
from webapp.views.reviews import AddReview, ReviewUpdate

app_name = 'products'

urlpatterns = [
    path('', IndexProducts.as_view(), name='index_products'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/review_add/', AddReview.as_view(), name='review_add'),
    path('review/<int:pk>/update/', ReviewUpdate.as_view(), name='review_update'),
]
