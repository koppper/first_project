from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=155)
    price = models.CharField(max_length=155)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
