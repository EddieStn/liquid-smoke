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
        product = get_object_or_404(Product, id=product_id)
        basket_item, created = BasketItem.objects.get_or_create(
            basket=basket, product=product)
        if product.discounted_price:
            basket_item.discounted_price = product.discounted_price
            basket_item.save()

    basket_items = basket.items.all()
    basket_total = sum(item.get_total_price() for item in basket_items)

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
        basket_item_id = request.POST.get('basket_item_id')
        basket_item = get_object_or_404(BasketItem, id=basket_item_id)

        if action == 'increase':
            basket_item.quantity += 1
        elif action == 'decrease':
            basket_item.quantity = max(1, basket_item.quantity - 1)
        elif action == 'delete':
            basket_item.delete()
        else:
            try:
                new_quantity = int(request.POST.get('quantity'))
                difference = new_quantity - basket_item.quantity
                basket_item.quantity = max(1, new_quantity)
            except (TypeError, ValueError):
                pass

        basket_item.save()

    return redirect('view_basket')


@login_required
def remove_from_basket(request, basket_item_id):
    basket_item = get_object_or_404(BasketItem, id=basket_item_id)

    if basket_item.basket.user != request.user:
        return redirect('view_basket')

    basket_item.delete()

    return redirect('view_basket')
