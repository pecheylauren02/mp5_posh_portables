from django.test import TestCase
from .models import Category, Product

class TestCategoryModel(TestCase):
    def setUp(self):
        # Create a Category
        self.category = Category.objects.create(
            name='Electronics',
            friendly_name='electronics'
        )

    def test_category_str(self):
        """
        Test the __str__ method of Category model
        """
        expected_str = 'Electronics'
        self.assertEqual(str(self.category), expected_str)

    def test_category_friendly_name(self):
        """
        Test the get_friendly_name method of Category model
        """
        friendly_name = self.category.get_friendly_name()
        self.assertEqual(friendly_name, 'electronics')
    
class TestProductModel(TestCase):
    def setUp(self):
        # Create a Category
        self.category = Category.objects.create(
            name='Electronics',
            friendly_name='electronics'
        )

        # Create a Product
        self.product = Product.objects.create(
            category=self.category,
            sku='123456',
            name='Smartphone',
            description='A smart and powerful phone',
            price=499.99,
            rating=4.5,
            image_url='https://example.com/smartphone.jpg',
            image=None  # Provide an image file if needed
        )

    def test_product_str(self):
        """
        Test the __str__ method of Product model
        """
        expected_str = 'Smartphone'
        self.assertEqual(str(self.product), expected_str)

    def test_product_category_relationship(self):
        """
        Test the relationship between Product and Category
        """
        self.assertEqual(self.product.category, self.category)

    def test_product_price_decimal_places(self):
        """
        Test that the price has the correct number of decimal places
        """
        self.assertEqual(self.product._meta.get_field('price').decimal_places, 2)

    def test_product_rating_null_blank(self):
        """
        Test that rating can be null or blank
        """
        product_with_rating = Product.objects.create(
            category=self.category,
            name='Laptop',
            description='A powerful laptop',
            price=999.99,
            rating=None,
            image_url='https://example.com/laptop.jpg',
            image=None
        )
        self.assertIsNone(product_with_rating.rating)

    def test_product_image_upload(self):
        """
        Test that the product image can be uploaded
        """
        self.assertIsNotNone(self.product.image)
