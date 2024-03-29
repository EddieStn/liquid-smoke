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
    return redirect('checkout')


def apply_coupon(request):
    now = timezone.now()
    coupon_code = request.POST.get('coupon_code')
    orders = Order.objects.filter(user=request.user)
    order = orders.first()
    coupon_form = CouponForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        active=True,
                                        valid_from__lte=now,
                                        valid_to__gte=now)
            order.coupon = coupon
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
    order.save()
    return redirect('checkout')


def checkout_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
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
                order.discount = order.get_total_cost() * (coupon.discount / 100)
                order.save()
                messages.success(request, "Coupon applied successfully!")
                messages.success(request, "Order created successfully!")
            else:
                messages.success(request, "Order created successfully!")

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
        if 'apply_coupon' in request.GET:
            coupon_form = CouponForm(request.GET)
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

    if coupon_id:
        del request.session['coupon_id']

    context = {
        'order_form': order_form,
        'basket_items': basket_items,
        'basket_total': basket_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'coupon': coupon,
    }
    return render(request, 'checkout/checkout.html', context)
