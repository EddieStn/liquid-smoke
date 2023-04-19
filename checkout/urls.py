from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('order_detail/<order_number>', views.order_detail,
         name='order_detail'),
]
