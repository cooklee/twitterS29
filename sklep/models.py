from django.db import models

# Create your models here.
from twitter_app.models import User


class Product(models.Model):
    name = models.CharField(max_length=123)
    price = models.FloatField()
    buyers = models.ManyToManyField(User, through='Cart')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
