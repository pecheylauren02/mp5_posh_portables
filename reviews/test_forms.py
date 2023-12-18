from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    """
    Review Form Tests
    """

    def test_review_title_required(self):
        """ Test the review title is a required field """
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_review_content_required(self):
        """ Test the review content is a required field """
        form = ReviewForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')