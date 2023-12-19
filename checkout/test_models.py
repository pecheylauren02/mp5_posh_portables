from django.test import TestCase

from .models import Order, OrderLineItem
from products.models import Product, Category


class TestCheckoutModels(TestCase):
    """
    Checkout Models Tests
    """

    def setUp(self):

        self.categoryTest = Category.objects.create(
            name="Keyboards",
            friendly_name="keyboards",
        )

        self.productTest1 = Product.objects.create(
            category=self.categoryTest,
            name="Laptop",
            description="Test description for Laptop",
            price=500,
            image='image-file'
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="Headphones",
            description="Test description for Headphones",
            price=20,
            image='image-file'
        )

        self.productTest3 = Product.objects.create(
            category=self.categoryTest,
            name="Monitor",
            description="Test description for Monitor",
            price=80,
            image='image-file'
        )

        self.productTest4 = Product.objects.create(
            category=self.categoryTest,
            name="ASUS Package",
            description="Test description for ASUS Package",
            price=120,
            image='image-file'
        )

        self.orderTest = Order.objects.create(
            order_number='1234567890',
            first_name="Test User",
            email="testemail@email.com",
            phone="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            city="Test City",
            county="Test County",
            postcode="AA11 2BB",
            country="GB",
        )

        self.orderLineItemTest1 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest1,
            quantity=1,
        )

        self.orderLineItemTest2 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest2,
            quantity=1,
        )

        self.orderLineItemTest3 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest3,
            quantity=10,
        )

        self.orderLineItemTest4 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest4,
            quantity=1,
        )

    def test_order_string_method(self):
        """ Tests the string method on the order model """
        order = Order(order_number='1234567890')
        self.assertEqual(str(order), order.order_number)
    
    def test_order_number(self):
        """ Test the order number """
        self.assertEqual(self.orderTest.order_number, '1234567890')

    def test_order_name(self):
        """ Test the order full name """
        self.assertEqual(self.orderTest.first_name, 'Test User')

    def test_order_email(self):
        """ Test the order email """
        self.assertEqual(self.orderTest.email, 'testemail@email.com')

    def test_order_phone(self):
        """ Test the order phone """
        self.assertEqual(self.orderTest.phone, '0123456789')