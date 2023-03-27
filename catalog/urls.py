from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.product, name='products'),
    # path('candles/', views.candles, name='candles'),
    # path('oils/', views.oils, name='oils'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
]
