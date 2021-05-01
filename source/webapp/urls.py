from django.urls import path
from webapp.views import (
    IndexProducts,
)

app_name = 'products'

urlpatterns = [
    path('', IndexProducts.as_view(), name='index_products'),
]
