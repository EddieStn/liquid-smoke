from django import forms
from catalog.models import Product


class AddToBasketForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean_product_id(self):
        product_id = self.cleaned_data['product_id']
        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError("Invalid product")
        return product_id
