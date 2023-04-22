from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from decimal import Decimal
from django.views.decorators.http import require_POST

from .forms import OrderForm, CouponForm
from catalog.models import Product
from basket.models import Basket, BasketItem
from .models import Order, OrderItem, Coupon
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe


@login_required
@require_POST
def apply_coupon(request):
    now = timezone.now()
    coupon_form = CouponForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        active=True,
                                        valid_from__lte=now,
                                        valid_to__gte=now)
            request.session['coupon_id'] = coupon.id
            messages.success(request, 'Coupon applied successfully')
        except Coupon.DoesNotExist:
            messages.error(request, 'Invalid coupon code')
        except Coupon.MultipleObjectsReturned:
            messages.error(request, 'Multiple coupons with the same code')
        except Coupon.InactiveCoupon:
            messages.error(request, 'Coupon is not active')
        except Coupon.ExpiredCoupon:
            messages.error(request, 'Coupon has expired')
    return redirect('checkout')


@require_POST
def cache_checkout_data(request):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order_form = OrderForm()
    coupon_id = request.session.get('coupon_id')
    coupon = None
    if coupon_id:
        coupon = get_object_or_404(Coupon, id=coupon_id, active=True,
                                   valid_from__lte=timezone.now(),
                                   valid_to__gte=timezone.now())
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
            if coupon:
                order.coupon = coupon
                order.discount = order.get_total_cost() * (
                    coupon.discount / 100)
                order.save()
                messages.success(request, "Coupon applied successfully!")
                messages.success(request, "Order created successfully!")
            else:
                messages.success(request, "Order created successfully!")

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'order_detail', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

    else:
        basket = get_object_or_404(Basket, user=request.user)
        basket_items = basket.items.all()
        coupon_saved = 0

        if not basket:
            messages.error(request, "Your basket is empty")
            return redirect(reverse('products'))
        if coupon:
            total = sum(item.get_total_price() for item in basket_items)
            basket_total = total - round(
                total * Decimal(coupon.discount / 100), 2)
            coupon_saved = total - basket_total
        else:
            basket_total = sum(item.get_total_price() for item in basket_items)

        stripe_total = round(basket_total * 100)
        stripe.api_key = stripe_secret_key
        try:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
        except stripe.error.InvalidRequestError as e:
            messages.info(request, "You basket is empty")
            return redirect(reverse('home'))

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                last_order = Order.objects.filter(user=request.user).order_by('-created_at').first()

                if last_order:
                    initial_data = {
                        'first_name': last_order.first_name,
                        'last_name': last_order.last_name,
                        'email': last_order.email,
                        'phone_number': profile.phone_number,
                        'address_line_1': profile.address_line_1,
                        'address_line_2': profile.address_line_2,
                        'city': profile.city,
                        'country': profile.country,
                        'postcode': profile.postcode,
                    }
                    order_form = OrderForm(initial=initial_data)
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        coupon_form = CouponForm()

    if coupon_id:
        del request.session['coupon_id']

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'coupon_form': coupon_form,
        'basket_items': basket_items,
        'basket_total': basket_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'coupon': coupon,
        'coupon_saved': coupon_saved,
    }
    return render(request, 'checkout/checkout.html', context)


@login_required
def order_detail(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number,
                              user=request.user)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'phone_number': order.phone_number,
                'country': order.country,
                'postcode': order.postcode,
                'city': order.city,
                'address_line_1': order.address_line_1,
                'address_line_2': order.address_line_2,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
