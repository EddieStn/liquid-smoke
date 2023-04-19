from django.contrib import admin
from .models import Order, OrderItem, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'get_total_cost', )
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number',
                    'address_line_1', 'city', 'postcode', 'country', 'status',
                    'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'updated_at']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']
    list_filter = ['order']


admin.site.register(Coupon)
