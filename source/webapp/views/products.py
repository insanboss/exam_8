from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexProducts(ListView):
    template_name = 'products/index_products.html'
    context_object_name = 'products'
    model = Product


class ProductView(DetailView):
    template_name = 'products/product_view.html'
    model = Product
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products:index_products')
