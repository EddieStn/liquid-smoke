from .models import Basket


def basket_total(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        basket_items = basket.items.all()
        if basket:
            return {'basket_total':
                    sum(item.get_total_price() for item in basket_items)}
    return {'basket_total': 0}
