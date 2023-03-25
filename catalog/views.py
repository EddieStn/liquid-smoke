from django.shortcuts import render, get_object_or_404
from .models import Candle, EssentialOil, Review, Product
from .forms import ReviewForm, AddToBasketForm


def product(request):
    """ A view to display the store products page """
    candles = Candle.objects.all()
    essential_oils = EssentialOil.objects.all()
    context = {
        'candles': candles,
        'essential_oils': essential_oils,
    }
    return render(request, 'home/index.html', context)


def product_details(request, product_id):
    # Get the product with the given ID or return 404
    product = get_object_or_404(Product, pk=product_id)

    # Handle ReviewForm submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Create a new review object
            review = Review(
                product=product,
                user=request.user,
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                rating=form.cleaned_data['rating']
            )
            review.save()
    else:
        # Display a blank form for the user to fill in
        form = ReviewForm()

    # Handle AddToBasketForm submission
    if request.method == 'POST':
        basket_form = AddToBasketForm(product, request.POST)
        if basket_form.is_valid():
            # Add the product to the user's basket
            quantity = basket_form.cleaned_data['quantity']
            # Your implementation to add to basket

    else:
        # Display a blank form for the user to fill in
        basket_form = AddToBasketForm(product=product)

    # Get the reviews for the product
    reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'basket_form': basket_form
    }
    return render(request, 'home/product_details.html', context)
