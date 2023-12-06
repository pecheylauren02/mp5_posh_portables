from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',
                  'phone','street_address1', 'streetaddress2',
                  'city', 'postcode', 'country', 'county',)