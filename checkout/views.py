from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from catalog.models import Product
from basket.models import Basket, BasketItem
from .models import Order, OrderItem, Coupon

import stripe


@login_required
def checkout_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = get_object_or_404(Basket, user=request.user)

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            basket_items = basket.items.all()
            for item in basket_items:
                order_item = order.items.create(
                    product=item.product,
                    price=item.get_item_price(),
                    quantity=item.quantity
                )
                order_item.save()
            if order.coupon:
                order.discount = order.get_total_cost() * (
                    order.coupon.discount / 100
                )
                order.save()
                messages.success(request, "Order created successfully!")
                return redirect('order_detail', args=[order.order_number])

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'order_detail', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

    else:
        basket = get_object_or_404(Basket, user=request.user)
        basket_items = basket.items.all()
        if not basket:
            messages.error(request, "Your basket is empty")
            return redirect(reverse('products'))

        basket_total = sum(item.get_total_price() for item in basket_items)
        stripe_total = round(basket_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'basket_items': basket_items,
        'basket_total': basket_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


@login_required
def order_detail(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number,
                              user=request.user)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    order_items = order.items.all()
    basket = get_object_or_404(Basket, user=request.user)
    basket_items = basket.items.all()
    basket_items.delete()

    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'checkout/order_detail.html', context)
