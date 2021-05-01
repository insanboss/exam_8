from django.views.generic import ListView, DetailView

from webapp.models import Product


class IndexProducts(ListView):
    template_name = 'products/index_products.html'
    context_object_name = 'products'
    model = Product


class ProductView(DetailView):
    template_name = 'products/product_view.html'
    model = Product
    context_object_name = 'product'

