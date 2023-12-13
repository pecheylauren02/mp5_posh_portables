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

        # Set autofocus on the content input
        self.fields['content'].widget.attrs['autofocus'] = True

        # Set aria-labels on input fields
        self.fields['title'].widget.attrs['aria-label'] = 'Title of your review'
        self.fields['content'].widget.attrs['aria-label'] = 'Write your review here'
        self.fields['rating'].widget.attrs['aria-label'] = 'Rating: Choose a value between 1-5'

        for field in self.fields:
            # Asterisk for required fields
            placeholder = f'{placeholders[field]} *' if self.fields[field].required else placeholders[field]

            # Set placeholders on inputs
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add custom styling classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'custom-form-field mb-3 px-3 py-2 font-body text-dark')

            # Removes input labels
            self.fields[field].label = False

        # Hidden input field for rating score
        # Accessible to screen readers
        self.fields['rating'].widget.attrs['class'] = (
            'rating-field visually-hidden')
