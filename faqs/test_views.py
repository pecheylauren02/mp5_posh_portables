from django.test import TestCase
from django.contrib.auth.models import User

from .models import Faq


class TestFaqsViews(TestCase):
    """
    FAQ Views Tests
    """

    def setUp(self):
        """
        Creates test objects for FAQs app
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

        self.faqTest = Faq.objects.create(
            question="Test Question",
            answer="Test Answer",
        )

    def test_faqs_page(self):
        """ Test FAQs view """
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')

    def test_add_faq_page_for_logged_out_user(self):
        """ Test create faq view for logged out user """

        response = self.client.get('/faqs/create/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/faqs/create/')