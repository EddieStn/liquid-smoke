from django import forms
from .models import Review, Product, Candle, EssentialOil, Category


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'body', 'rating')
        labels = {
            'title': 'Title',
            'body': 'Body',
            'rating': 'Rating',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class CandleForm(forms.ModelForm):
    class Meta:
        model = Candle
        fields = ('name', 'description', 'price', 'discounted_price', 'image',
                  'is_available', 'categories', 'scent', 'burn_time')


class EssentialOilForm(forms.ModelForm):
    class Meta:
        model = EssentialOil
        fields = ('name', 'description', 'price', 'discounted_price', 'image',
                  'is_available', 'categories', 'scent', 'volume')
