from django import forms
from .models import Review


class AddToBasketForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_id'].initial = product.id
        self.fields['quantity'].widget.attrs['class'] = 'form-control'


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