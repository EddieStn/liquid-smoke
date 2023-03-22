from django.contrib import admin
from .models import Category, Product, Candle, EssentialOil, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'discounted_price',
        'image',
        'is_available',
    )
    inlines = [ReviewInline]


class CandleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'discounted_price',
        'image',
        'is_available',
        'scent',
        'burn_time',
    )


class OilsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'discounted_price',
        'image',
        'is_available',
        'scent',
        'volume',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'title', 'rating', 'approved')
    list_filter = ('approved',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

    approve_reviews.short_description = 'Approve selected reviews'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Candle, CandleAdmin)
admin.site.register(EssentialOil, OilsAdmin)
admin.site.register(Review, ReviewAdmin)
