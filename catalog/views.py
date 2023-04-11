from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from django.db.models.functions import Lower
from .models import Candle, EssentialOil, Review, Product
from .forms import ReviewForm, AddToBasketForm, CandleForm, \
    EssentialOilForm, ProductForm


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
    categories = None
    query = None
    sortkey = None
    direction = None

    if request.GET:
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
        'candles': candles,
        'essential_oils': essential_oils,
        'current_categories': categories,
        'search_term': query,
        'sortkey': sortkey,
        'direction': direction,
    }
    return render(request, 'home/products.html', context)


def product_details(request, product_id):
    """A view to display an individual product details"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        if 'review_form' in request.POST:
            # Handle ReviewForm submission
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = Review(
                    product=product,
                    user=request.user,
                    title=form.cleaned_data['title'],
                    body=form.cleaned_data['body'],
                    rating=form.cleaned_data['rating']
                )
                review.save()
        else:
            form = ReviewForm()

        if 'basket_form' in request.POST:
            # Handle AddToBasketForm submission
            basket_form = AddToBasketForm(product, request.POST)
            if basket_form.is_valid():
                # Add the product to the user's basket
                quantity = basket_form.cleaned_data['quantity']
                basket_url = reverse('add_to_basket_view', args=[product.id])
                return HttpResponseRedirect(f"{basket_url}?quantity={quantity}")
        else:
            basket_form = AddToBasketForm(product=product)

    else:
        form = ReviewForm()
        basket_form = AddToBasketForm(product=product)

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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        candle_form = CandleForm(request.POST, request.FILES)
        oil_form = EssentialOilForm(request.POST, request.FILES)
        if candle_form.is_valid():
            candle_form.save()
            messages.success(request, 'Successfully added product!')
            return redirect('add_product')
        elif oil_form.is_valid():
            oil_form.save()
            messages.success(request, 'Successfully added product!')
            return redirect('add_product')
        else:
            messages.error(request, 'Failed to add product. \
            Please ensure the form is valid.')
    else:
        candle_form = CandleForm()
        oil_form = EssentialOilForm()

    context = {
        'candle_form': candle_form,
        'oil_form': oil_form,
    }

    return render(request, 'home/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'home/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
