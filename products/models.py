from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

