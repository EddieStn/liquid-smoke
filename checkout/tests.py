from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    def test_form_has_correct_fields(self):
        form = OrderForm()
        expected_fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'address_line_1', 'address_line_2', 'city', 'country',
            'postcode'
        ]
        self.assertSequenceEqual(expected_fields, list(form.fields))

    def test_form_field_placeholders(self):
        form = OrderForm()
        expected_placeholders = {
            'first_name': 'First Name *',
            'last_name': 'Last Name *',
            'email': 'Email Address *',
            'phone_number': 'Phone Number *',
            'address_line_1': '123 Main St *',
            'address_line_2': 'Apartment, studio, or floor',
            'city': 'Town or City *',
            'country': 'Country *',
            'postcode': 'Postal Code *',
        }
        for field_name, expected_placeholder in expected_placeholders.items():
            self.assertEqual(form.fields[field_name].
                             widget.attrs['placeholder'], expected_placeholder)

    def test_form_field_classes(self):
        form = OrderForm()
        expected_classes = 'stripe-style-input'
        for field in form.fields.values():
            self.assertIn(expected_classes, field.widget.attrs['class'])

    def test_form_required_fields(self):
        form = OrderForm()
        required_fields = ['first_name', 'last_name', 'email', 'phone_number',
                           'address_line_1', 'city', 'country', 'postcode']
        for field_name in required_fields:
            self.assertTrue(form.fields[field_name].required)

    def test_form_labels(self):
        form = OrderForm()
        for field in form.fields.values():
            self.assertFalse(field.label)

    def test_form_first_name_autofocus(self):
        form = OrderForm()
        self.assertTrue(form.fields['first_name'].widget.attrs['autofocus'])
