from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    candles = models.ManyToManyField('Candle', blank=True)
    oils = models.ManyToManyField('EssentialOil', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def avg_rating(self):
        reviews = self.reviews.filter(approved=True)
        if reviews.count() > 0:
            return reviews.aggregate(Avg('rating'))['rating__avg']
        else:
            return None


class Candle(Product):
    scent = models.CharField(max_length=255)
    burn_time = models.CharField(max_length=50)


class EssentialOil(Product):
    scent = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    rating = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.name}"
