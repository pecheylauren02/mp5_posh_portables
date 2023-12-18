from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
from django.contrib.auth.models import User

from products.models import Product, Category
from reviews.models import Reviews


@freeze_time("2022-08-15")
class TestReviewsViews(TestCase):
    """
    Review Views Tests
    """

    def setUp(self):
        """
        Creates test objects for Reviews app
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
            is_featured=True,
            image='image-file'
        )

        self.reviewTest = Reviews.objects.create(
            product=self.productTest,
            user=userTest,
            title="test review title",
            content="test review content",
            rating=3,
            created_on=timezone.now(),
        )

        self.reviewTest2 = Reviews.objects.create(
            product=self.productTest,
            user=superuserTest,
            title="test review title 2",
            content="test review content 2",
            rating=5,
            created_on=timezone.now(),
        )
