from django import forms


class AddToBasketForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_id'].initial = product.id
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
