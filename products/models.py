from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField()
