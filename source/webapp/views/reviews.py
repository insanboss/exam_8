from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class AddReview(CreateView):
    model = Review
    template_name = 'reviews/review_create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('products:product_view', pk=product.pk)


class ReviewUpdate(UpdateView):
    model = Review
    template_name = 'reviews/review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('products:index_products')



