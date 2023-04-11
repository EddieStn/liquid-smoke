from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s basket"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE,
                               related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.basket.user.username}'s basket"
