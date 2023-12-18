from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Product Form Tests
    """

    def test_product_name_required(self):
        """ Test the product name is a required field """
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_description_required(self):
        """ Test the product description is a required field """
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_product_price_required(self):
        """ Test the product price is a required field """
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_not_required_fields(self):
        """ Test form is valid with empty non-required fields """
        form = ProductForm(
            {
                'name': 'test product',
                'description': 'test description',
                'price': '59.99',
                'delivery_charge': '',
                'category': '',
                'image': '',
            }
        )
        self.assertTrue(form.is_valid())
