from django.shortcuts import render
from .models import Candle, EssentialOil


def product(request):
    """ A view to display the store products page """
    candles = Candle.objects.all()
    essential_oils = EssentialOil.objects.all()
    context = {
        'candles': candles,
        'essential_oils': essential_oils,
    }
    return render(request, 'home/index.html', context)
