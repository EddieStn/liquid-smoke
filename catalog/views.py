from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from django.db.models.functions import Lower
from .models import Candle, EssentialOil, Review, Product, Category
from .forms import ReviewForm, CandleForm, \
    EssentialOilForm, ProductForm


def sort_products(request, products):
    """ A function to sort products based on user input """
    sort = request.GET.get('sort', '')
    if sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'rating_asc':
        products = products.annotate(
            avg_rating=Avg('reviews__rating')).order_by('avg_rating')
    elif sort == 'rating_desc':
        products = products.annotate(
            avg_rating=Avg('reviews__rating')).order_by('-avg_rating')

    return products


def search_products(request, products):
    """
    A function to search products based on user input.
    It accepts a request and a queryset of products,
    and returns a filtered queryset.
    """
    query = request.GET.get('q')

    if query:
        queries = Q(name__icontains=query) | Q(
            description__icontains=query) | Q(
            categories__name__icontains=query)
        products = products.filter(queries)

        if not products.exists():
            messages.warning(request, f"No results found for '{query}'.")
        else:
            messages.success(request, f"Products found for '{query}'.")

    return products


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    query = None

    if request.GET:
        products = search_products(request, products)

    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)


def product(request):
    """ A view to display the store products page """
    products = Product.objects.annotate(avg_rating=Avg('reviews__rating'))
    categories = Category.objects.all()
    query = None

    if request.GET:

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(categories__name=category)

        if 'type' in request.GET:
            p_type = request.GET['type']
            if p_type == 'candles':
                products = products.filter(
                    categories__name='Candles').order_by('name')
            elif p_type == 'essential_oils':
                products = products.filter(
                    categories__name='Essential Oils').order_by('name')
        products = sort_products(request, products)
        products = search_products(request, products)

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home/products.html', context)


def product_details(request, product_id):
    """A view to display an individual product details"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        if 'review_form' in request.POST:
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

    else:
        form = ReviewForm()

    reviews = Review.objects.filter(product=product, approved=True)

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'home/product_details.html', context)


def candles(request):
    """ A view to display only candles """
    candles = Candle.objects.all()

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            candles = candles.filter(category__name__in=categories)
        candles = sort_products(request, candles)
        candles = search_products(request, candles)

    num_products = candles.count()

    context = {
        'candles': candles,
        'num_products': num_products,
    }
    return render(request, 'home/candles.html', context)


def essential_oils(request):
    """ A view to display only essential_oils """
    essential_oils = EssentialOil.objects.all()

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            essential_oils = essential_oils.filter(
                category__name__in=categories)
        essential_oils = sort_products(request, essential_oils)
        essential_oils = search_products(request, essential_oils)

    num_products = essential_oils.count()

    context = {
        'essential_oils': essential_oils,
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
        messages.error(request, "Sorry, you don't have permission \
             to access this page.")
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
        messages.error(request, "Sorry, you don't have permission \
             to access this page.")
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
        messages.error(request, "Sorry, you don't have permission \
             to access this page.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def faq(request):
    """ Display the frequently asked questions page """
    return render(request, 'home/faq.html')
