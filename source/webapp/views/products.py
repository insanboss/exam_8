from django.views.generic import ListView

from webapp.models import Product


class IndexProducts(ListView):
    template_name = 'products/index_products.html'
    context_object_name = 'products'
    model = Product

