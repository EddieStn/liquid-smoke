from django.urls import path
from . import views


urlpatterns = [
     path('basket/', views.view_basket, name='view_basket'),
     path('add-to-basket/<int:product_id>/',
          views.add_to_basket, name='add_to_basket'),
     path('remove-from-basket/<int:basket_item_id>/',
          views.remove_from_basket, name='remove_from_basket'),
     path('update-basket/<int:basket_item_id>/',
          views.update_basket, name='update_basket'),
]
