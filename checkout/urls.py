from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/order_detail/<uuid:order_number>/',
         views.order_detail, name='order_detail'),
]
