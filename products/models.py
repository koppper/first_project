from django.db import models


class Products(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    products = models.ForeignKey(Products, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
