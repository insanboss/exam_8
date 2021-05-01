from django.contrib import admin

# Register your models here.
from webapp.models import Review, Product

admin.site.register(Product)
admin.site.register(Review)
