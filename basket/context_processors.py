from .models import Basket


def basket_total(request):
    """A function that calculates and returns the total price of the basket"""
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        if basket:
            basket_items = basket.items.all()
            return {'basket_total':
                    sum(item.get_total_price() for item in basket_items)}
    return {'basket_total': 0}
