from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=256)
    descriptiion = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_image")
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
