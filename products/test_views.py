from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product, Category
from checkout.models import Order, OrderLineItem


class TestProductsViews(TestCase):
    """
    Products Views Tests
    """

    def setUp(self):
        """
        Creates test objects for Products app
        """

        userTest = User.objects.create_user(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
        )
        userTest.save()

        superuserTest = User.objects.create_superuser(
            username="superuser1",
            password="super_password1",
            email='testsuperuseremail@email.com',
        )
        superuserTest.save()

        self.categoryTest = Category.objects.create(
            name="Keyboards",
            friendly_name="keyboards",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Gaming Keyboard",
            description="Test description for Gaming Keyboard",
            price=53.99,
        )

        self.productTest2 = Product.objects.create(
            category=self.categoryTest,
            name="Asus Laptop",
            description="Test description for Asus Laptop",
            price=4,
        )

        self.productTest3 = Product.objects.create(
            category=self.categoryTest,
            name="Old Product",
            description="Test description for Old Product",
            price=4,
        )

        self.orderTest = Order.objects.create(
            order_number='1234567890',
            first_name="Test User",
            last_name="Test User Surname",
            email="testemail@email.com",
            phone="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            city="Test City",
            county="Test County",
            country="GB",
        )

        self.orderLineItemTest1 = OrderLineItem.objects.create(
            order=self.orderTest,
            product=self.productTest2,
            quantity=1,
        )

    def test_products_page(self):
        """ Test products view """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page_with_invalid_product(self):
        """ Test product detail view works with an invalid product """
        response = self.client.get('/99/')
        self.assertEqual(response.status_code, 404)

    def test_add_product_page_for_logged_out_user(self):
        """ Test add product view for logged out user """

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/add/')

    def test_add_product_page_for_unauthorised_user(self):
        """ Test add product view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_add_product_page_for_superuser(self):
        """ Test add product view for authorised user (superuser) """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')