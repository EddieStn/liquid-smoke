from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Basket, BasketItem


@login_required
def view_basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)

    return render(request, 'basket/view_basket.html', {'basket': basket})


@login_required
def add_to_basket_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user)

    basket_item, item_created = BasketItem.objects.get_or_create(
        basket=basket, product=product)

    if not item_created:
        basket_item.quantity += 1
        basket_item.save()

    return redirect('view_basket')


@login_required
def remove_from_basket(request, basket_item_id):
    basket_item = get_object_or_404(BasketItem, id=basket_item_id)

    if basket_item.basket.user != request.user:
        return redirect('view_basket')

    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()

    return redirect('view_basket')
