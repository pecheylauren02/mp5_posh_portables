from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """
    return render(request, 'shopping_cart/shopping_cart.html')

def add_to_shopping_cart(request, item_id):
    """ Add a quantity of a specific product to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in shopping_cart:
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)

def adjust_shopping_cart(request, item_id):
    """ Adjust a quantity of a specific product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
    else:
        shopping_cart.pop[item_id]

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_shopping_cart'))
