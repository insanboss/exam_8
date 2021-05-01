from django import forms

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'categories', 'description', 'avatar']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating',]
