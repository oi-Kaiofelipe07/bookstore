from django.db import models

from product.models.category import Category


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)