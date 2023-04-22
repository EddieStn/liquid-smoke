from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserProfile


@login_required()
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile
        }
    return render(request, 'profiles/profiles.html', context)
