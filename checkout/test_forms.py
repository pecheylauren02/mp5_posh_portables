from django.test import TestCase
from .forms import OrderForm

class OrderFormTest(TestCase):
    def test_empty_form_submission(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertGreater(len(form.errors), 0)

    def test_valid_form_submission(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'street_address1': '123 Main St',
            'city': 'City',
            'postcode': '12345',
            'country': 'US',
            'county': 'County',
        }
        form = OrderForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_email_address(self):
        data = {'email': 'invalid-email'}
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_missing_required_field(self):
        data = {'first_name': 'John'}
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

    def test_autofocus_check(self):
        form = OrderForm()
        self.assertEqual(form.fields['first_name'].widget.attrs.get('autofocus'), True)

    def test_css_class_check(self):
        form = OrderForm()
        for field in form.fields:
            self.assertEqual(form.fields[field].widget.attrs.get('class'), 'stripe-style-input')

    def test_label_check(self):
        form = OrderForm()
        for field in form.fields:
            self.assertFalse(form.fields[field].label)

    def test_field_order_check(self):
        form = OrderForm()
        expected_order = ['first_name', 'last_name', 'email', 'phone', 'street_address1', 'street_address2', 'city', 'postcode', 'country', 'county']
        self.assertEqual(list(form.fields), expected_order)

    def test_optional_field_placeholder_check(self):
        form = OrderForm()
        self.assertEqual(form.fields['street_address2'].widget.attrs.get('placeholder'), 'Street Address 2')
