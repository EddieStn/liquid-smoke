from django.urls import path
from .views import add_to_basket_view, remove_from_basket, view_basket

app_name = 'basket'

urlpatterns = [
    path('add_to_basket/<int:product_id>/',
         add_to_basket_view, name='add_to_basket_view'),
    path('remove-from-basket/<int:basketitem_id>/',
         remove_from_basket, name='remove_from_basket'),
    path('basket/', view_basket, name='view_basket'),
]
