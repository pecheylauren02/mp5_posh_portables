from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Profile Form Tests
    """

    def test_not_required_fields(self):
        """ Test User Profile form is valid with empty non-required fields """
        form = UserProfileForm(
            {
                'default_street_address1': '',
                'default_street_address2': '',
                'default_city': '',
                'default_county': '',
                'default_postcode': '',
                'default_country': '',
                'default_phone': '',
            }
            )
        self.assertTrue(form.is_valid())

    def test_user_in_excludes_in_form_metaclass(self):
        """
        Test that 'user' field is excluded from the form's Meta
        """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
