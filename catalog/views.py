from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from django.db.models.functions import Lower
from .models import Candle, EssentialOil, Review, Product
from .forms import ReviewForm, AddToBasketForm


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    candles = Candle.objects.all()
    essential_oils = EssentialOil.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria")
            return redirect(reverse('home'))

        queries = Q(name__icontains=query) | Q(
                    description__icontains=query)
        products = products.filter(queries)
        candles = candles.filter(queries)
        essential_oils = essential_oils.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'candles': candles,
        'essential_oils': essential_oils,
    }
    return render(request, 'home/index.html', context)


def product(request):
    """ A view to display the store products page """
    products = Product.objects.annotate(avg_rating=Avg('reviews__rating'))
    candles = Candle.objects.all()
    essential_oils = EssentialOil.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)
            candles = candles.filter(queries)
            essential_oils = essential_oils.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'candles': candles,
        'essential_oils': essential_oils,
    }
    return render(request, 'home/products.html', context)


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
    reviews = Review.objects.filter(product=product, approved=True)

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'basket_form': basket_form
    }
    return render(request, 'home/product_details.html', context)


def candles(request):
    """ A view to display only candles """
    candles = Candle.objects.all()
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            candles = candles.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('candles'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            candles = candles.filter(queries)

    num_products = candles.count()

    context = {
        'candles': candles,
        'search_term': query,
        'num_products': num_products
    }
    return render(request, 'home/candles.html', context)


def essential_oils(request):
    """ A view to display only essential_oils """
    essential_oils = EssentialOil.objects.all()
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            essential_oils = essential_oils.filter(
                category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('essential_oils'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            essential_oils = essential_oils.filter(queries)

    num_products = essential_oils.count()

    context = {
        'essential_oils': essential_oils,
        'search_term': query,
        'num_products': num_products
    }
    return render(request, 'home/essential_oils.html', context)


def specials(request):
    """A view to display items on sale"""
    discounted_products = Product.objects.filter(
        discounted_price__isnull=False)

    num_products = discounted_products.count()

    context = {
        'discounted_products': discounted_products,
        'num_products': num_products,
    }
    return render(request, 'home/specials.html', context)
