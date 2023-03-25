from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product, name='home'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
]
