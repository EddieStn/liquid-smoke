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
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2,
                                           null=True, blank=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_item_price(self):
        return self.discounted_price \
                if self.discounted_price is not None else self.product.price

    def get_total_price(self):
        return self.quantity * self.get_item_price()

    def save(self, *args, **kwargs):
        if self.product.discounted_price:
            self.discounted_price = self.product.discounted_price
        super().save(*args, **kwargs)
