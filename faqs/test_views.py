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

    def test_create_faq_page_for_logged_out_user(self):
        """ Test create faq view for logged out user """

        response = self.client.get('/faqs/create/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/faqs/create/')

    def test_create_faqs_page_for_unauthorised_user(self):
        """ Test create faqs view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/create/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_create_faq_page_for_superuser(self):
        """ Test create faq view for authorised user (superuser) """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/create_faq.html')

    def test_update_faq_page_for_logged_out_user(self):
        """ Test update faq view for logged out user """

        response = self.client.get('/faqs/update/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/faqs/update/1/')

    def test_update_faq_page_for_unauthorised_user(self):
        """ Test update faq view for logged in user (not superuser) """

        logged_in = self.client.login(
            username='user1', password='password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/update/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/faqs/')

    def test_update_valid_faq_page_for_superuser(self):
        """
        Test update faq view for authorised user (superuser)
        With a valid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/update/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/update_faq.html')

    def test_update_invalid_faq_page_for_superuser(self):
        """
        Test update faq view for authorised user (superuser)
        With an invalid faq id
        """

        logged_in = self.client.login(
            username='superuser1', password='super_password1')
        self.assertTrue(logged_in)

        response = self.client.get('/faqs/update/99/')
        self.assertEqual(response.status_code, 404)

    def test_remove_faq_view_for_logged_out_user(self):
        """
        Checks remove faq view for logged out user
        """

        response = self.client.get('/faqs/remove/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/faqs/remove/1/')
