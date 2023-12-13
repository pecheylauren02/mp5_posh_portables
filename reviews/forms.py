from django import forms
from .models import Reviews


class CustomReviewForm(forms.ModelForm):
    """
    Form for user to make reviews (including Add and Edit)
    """
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Set placeholder values
        placeholders = {
            'title': 'Enter the product name',
            'content': 'Share your thoughts on this product...',
            'rating': 0
        }
