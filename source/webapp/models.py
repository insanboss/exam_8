from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
category_choices = [('food', 'еда'), ('household_products', 'бытовые товары'), ('garden_staff', 'товары для огорода'),
                    ('other', 'разное')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    categories = models.CharField(max_length=50, null=False, blank=False, choices=category_choices, default='other',
                                  verbose_name='категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    avatar = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Аватар')


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='profile',
                               on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Текст отзыва', )
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name='review',
                                verbose_name='продукт')
    rating = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        verbose_name='Оценка'
     )
    is_moderated = models.BooleanField(null=True, blank=True, verbose_name='промодерировано')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
