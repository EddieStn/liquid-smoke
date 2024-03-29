from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'address_line_1': '123 Main St',
            'address_line_2': 'Apartment, studio, or floor',
            'city': 'Town or City',
            'country': 'Country',
            'postcode': 'Postal Code',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
