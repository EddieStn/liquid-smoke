from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.forms import OrderForm
from catalog.models import Product
from basket.models import Basket, BasketItem
from .models import Order


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


class TestCheckoutView(TestCase):
    LOGIN_URL = '/accounts/login/'

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.product = Product.objects.create(name='Test Product', price=10)
        self.basket = Basket.objects.create(user=self.user)
        self.basket_item = BasketItem.objects.create(
            basket=self.basket, product=self.product, quantity=1)

    def test_checkout_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Total: $10.00')

    def test_checkout_view_post(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'address_line_1': '123 Main St',
            'city': 'New York',
            'postcode': '10001',
            'country': 'US',
        }
        response = self.client.post(reverse('checkout'), data=data)
        order = Order.objects.get(first_name='John')
        self.assertRedirects(response, reverse(
            'order_confirmation', kwargs={'order_number': order.order_number}))
        self.assertEqual(Order.objects.count(), 1)

        new_order = Order.objects.last()

        self.assertEqual(new_order.user, self.user)
        self.assertEqual(new_order.first_name, 'John')
        self.assertEqual(new_order.last_name, 'Doe')
        self.assertEqual(new_order.email, 'johndoe@example.com')
        self.assertEqual(new_order.phone_number, '1234567890')
        self.assertEqual(new_order.address_line_1, '123 Main St')
        self.assertEqual(new_order.city, 'New York')
        self.assertEqual(new_order.postcode, '10001')
        self.assertEqual(new_order.country, 'US')
        self.assertEqual(new_order.items.count(), 1)

        order_item = new_order.items.first()

        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.price, self.product.price)
        self.assertEqual(order_item.quantity, 1)

        basket_items = self.basket.items.all()
        self.assertEqual(basket_items.count(), 0)

        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('home'))
