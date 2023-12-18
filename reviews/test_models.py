from django.test import TestCase
from datetime import date
from django.utils import timezone

from products.models import Product, Category
from django.contrib.auth.models import User
from reviews.models import Reviews


class TestReviewModels(TestCase):
    """
    Reviews Model Tests
    """

    def setUp(self):
        """
        Creates test objects for Reviews app
        """

        self.categoryTest = Category.objects.create(
            name="keyboards",
            friendly_name="keyboards",
        )

        self.productTest = Product.objects.create(
            category=self.categoryTest,
            name="Gaming Keyboard",
            description="Test description for Gaming Keyboard",
            price=29.99,
            is_featured=True,
        )

        self.userTest = User.objects.create(
            username="user1",
            password="password1",
            email='testuseremail@email.com',
        )

        self.reviewTest = Review.objects.create(
            product=self.productTest,
            user=self.userTest,
            title="test review title",
            content="test review content",
            rating=3,
            created_on=timezone.now(),
        )
