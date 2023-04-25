from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required()
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile,
        'user_first_name': request.user.first_name,
        'user_last_name': request.user.last_name,
        'user_email': request.user.email,
    }

    return render(request, 'profiles/profiles.html', context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    messages.info(request, 'You are looking at past order confirmations')
    context = {
        'orders': orders,
    }
    return render(request, 'profiles/order_history.html', context)
