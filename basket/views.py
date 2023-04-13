from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Basket, BasketItem
from .forms import AddToBasketForm


@login_required
def view_basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    product_id = request.GET.get('product_id')
    if product_id is not None:
        item, _ = BasketItem.objects.get_or_create(basket=basket, product_id=product_id)
    basket_items = basket.items.all()
    basket_total = sum(
        item.product.price * item.quantity if item.product else 0 for item in basket_items)
    context = {
        'basket_items': basket_items,
        'basket_total': basket_total,
    }
    return render(request, 'basket/view_basket.html', context)


@login_required
def add_to_basket(request, product_id):
    if request.method == 'POST':
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            basket, _ = Basket.objects.get_or_create(user=request.user)
            item, created = BasketItem.objects.get_or_create(
                basket=basket, product_id=product_id)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()
            return redirect('view_basket')
    else:
        form = AddToBasketForm()
    return render(request, 'catalog/product_details.html', {'form': form})


@login_required
def update_basket(request, basket_item_id):
    basket_item = get_object_or_404(BasketItem, id=basket_item_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'increase':
            basket_item.quantity += 1
        elif action == 'decrease':
            basket_item.quantity -= 1

            if basket_item.quantity <= 0:
                # If the quantity is zero or negative, remove the item from the basket
                basket_item.delete()

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
