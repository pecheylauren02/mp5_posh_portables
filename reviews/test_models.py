from django.test import TestCase
from datetime import date
from django.utils import timezone
from freezegun import freeze_time

from products.models import Product, Category
from django.contrib.auth.models import User
from reviews.models import Reviews


@freeze_time("2023-12-18")
class TestReviewModels(TestCase):
    """
    Reviews Model Tests
    """

    def setUp(self):
        """
        Creates test objects for Reviews app
        """

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

        self.userTest = User.objects.create(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
        )

        self.reviewTest = Reviews.objects.create(
            product=self.productTest,
            user=self.userTest,
            title="test review title",
            content="test review content",
            rating=3,
            created_on=timezone.now(),
        )

    def test_review_string_method(self):
        """ Tests the string method on the review model """
        review = Reviews(title='test review title',
                         user=self.userTest, product=self.productTest)
        self.assertEqual(str(review), 'test review title by user1 for Gaming Keyboard')

    def test_review_title(self):
        """ Test the review title """
        self.assertEqual(self.reviewTest.title, 'test review title')

    def test_review_content(self):
        """ Test the review content """
        self.assertEqual(self.reviewTest.content, 'test review content')

    def test_review_rating(self):
        """ Test the review rating """
        self.assertEqual(self.reviewTest.rating, 3)

    def test_review_created_on(self):
        """ Test the review content """
        self.assertEqual(self.reviewTest.created_on, date(2023, 12, 18))

    def test_review_product_name(self):
        """ Test the review product """
        self.assertEqual(self.reviewTest.product.name, 'Gaming Keyboard')

    def test_review_product_category(self):
        """ Test the review product category """
        self.assertEqual(self.reviewTest.product.category.name, 'Keyboards')
