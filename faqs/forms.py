from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    """
    Form to create and update FAQs
    """

    class Meta:
        model = Faq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets placeholder values
        placeholders = {
            'question': 'Question',
            'answer': 'Answer'
        }