from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
from django.contrib.auth.models import User

from products.models import Product, Category
from reviews.models import Reviews


@freeze_time("2023-12-18")
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

    def test_create_reviews_page_for_authorized_user(self):
        """ Test create_review view for logged in user"""

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/reviews/create_reviews/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/create_reviews.html')

    def test_create_reviews_page_for_logged_out_user(self):
        """
        Checks create_review redirects to login
        if user is not logged in
        """

        response = self.client.get('/reviews/create_reviews/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=%2Freviews%2Fcreate_reviews%2F1')

    def test_update_reviews_page_for_authorized_user(self):
        """ Test update_reviews view for logged in user"""

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/reviews/update_reviews/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/update_reviews.html')

    def test_update_reviews_page_for_logged_out_user(self):
        """
        Checks update_reviews redirects to login
        if user is not logged in
        """

        response = self.client.get('/reviews/update_reviews/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=%2Freviews%2Fupdate_reviews%2F1%2F')

    def test_update_reviews_page_for_unauthorized_user(self):
        """
        Checks update_reviews redirects to product_details
        if user is not author of review
        """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/reviews/update_reviews/2/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/products/1')

    def test_update_other_user_review_page_for_superuser(self):
        """
        Checks update_reviews redirects to product_details
        if superuser is not author of review
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/reviews/update_reviews/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/products/1')

    def test_remove_reviews_view_for_logged_out_user(self):
        """
        Checks remove review redirects to login
        if user is not logged in
        """

        response = self.client.get('/reviews/remove_review/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=%2Freviews%2Fremove_review%2F1%2F'
        )

    def test_remove_reviews_page_for_unauthorized_user(self):
        """
        Checks remove_reviews redirects to product_details
        if user is not author of review
        """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/reviews/remove_review/2/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/products/1')
