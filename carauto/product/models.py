from django.db import models
from rest_framework import serializers


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100)
    brief = models.CharField(max_length = 100)
    status_category = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    image = models.CharField(max_length = 255)
    price = models.IntegerField()
    brief = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    status_product = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Variation(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    sale_price = models.IntegerField(default = 0)
    inventory = models.IntegerField(default = 0)
    status_variation = models.BooleanField(default = True)

    def __str__(self):
        return self.name
