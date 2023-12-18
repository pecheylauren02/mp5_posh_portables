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
