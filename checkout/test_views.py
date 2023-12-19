from django.test import TestCase

from .models import Order
from products.models import Product, Category


class TestCheckoutViews(TestCase):
    """
    Checkout Views Tests
    """

    def setUp(self):

        self.categoryTest = Category.objects.create(
            name="Keyboards",
            friendly_name="keyboards",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Samsung Monitor",
            description="Test description for Samsung Monitor",
            price=53.99,
            image='image-file'
        )

        self.order = Order.objects.create(
            order_number='1234567890',
            first_name="Test User",
            email="testemail@email.com",
            phone="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            city="Test City",
            county="Test County",
            country="US",
        )

    def test_get_checkout_page_with_empty_cart(self):
        """ test checkout page redirects to products with empty cart """

        response = self.client.get('/checkout/')
        self.assertTrue(response, '/products')

    def test_get_checkout_page_with_shopping_cart_items(self):
        """ test checkout page view with bag items """

        session = self.client.session
        session['shopping_cart'] = {str(self.productTest.id): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')