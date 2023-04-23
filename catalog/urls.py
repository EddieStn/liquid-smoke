from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='home'),
     path('catalog/faq/', views.faq, name='faq'),
     path('products/', views.product, name='products'),
     path('candles/', views.candles, name='candles'),
     path('essential_oils/', views.essential_oils, name='essential_oils'),
     path('specials/', views.specials, name='specials'),
     path('product/<int:product_id>/',
          views.product_details, name='product_details'),
     path('add_product/', views.add_product, name='add_product'),
     path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
     path('delete/<int:product_id>/', views.delete_product,
          name='delete_product'),
]
