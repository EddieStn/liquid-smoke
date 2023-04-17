import uuid
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from catalog.models import Product


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                   MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

    def is_valid(self):
        return self.active \
            and self.valid_from <= timezone.now() <= self.valid_to


class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='P')
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True,
                               blank=True, on_delete=models.SET_NULL)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                   validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Order #{self.order_number}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        for item in self.items.all():
            if item.product.discounted_price:
                total_cost -= item.get_cost()
                total_cost += item.quantity * item.product.discounted_price
        if self.coupon:
            total_cost *= (1 - (self.coupon.discount / Decimal('100')))
        return total_cost


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
