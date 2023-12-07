from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})

    if not shopping_cart:
        messages.error(request, "Your shopping cart is empty at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OKdbyHZ7jyXnuyb2YonXHz3B95UiQ0G17U8zvGUWOOL3hkCWrT5hbTgZRLyQTfQoRpGQGx0taaMkPEcfVNhFsaP000Pm6yWxH',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)