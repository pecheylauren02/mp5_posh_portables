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

        # Sets autofocus on first input
        self.fields['question'].widget.attrs['autofocus'] = True

        # Sets aria-labels on inputs
        self.fields['question'].widget.attrs['aria-label'] = 'FAQ Question'
        self.fields['answer'].widget.attrs['aria-label'] = 'FAQ Answer'