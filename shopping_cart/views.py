from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """
    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_shopping_cart(request, item_id):
    """ Add a quantity of a specific product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in shopping_cart:
        shopping_cart[item_id] += quantity
        messages.success(request, f'UPDATED {product.name} QTY TO {shopping_cart[item_id]}!')
    else:
        shopping_cart[item_id] = quantity
        messages.success(request, f'ADDED {product.name} TO YOUR CART!')

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)


def adjust_shopping_cart(request, item_id):
    """ Adjust a quantity of a specific product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
        messages.success(request, f'UPDATED {product.name} TO YOUR CART!')
    else:
        shopping_cart.pop(item_id)

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_shopping_cart'))


def remove_from_shopping_cart(request, item_id):
    """ Removes the item from the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in shopping_cart:
        shopping_cart.pop(item_id)
        messages.success(request, f'REMOVED {product.name} FROM YOUR CART!')
        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    else:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

    return redirect(reverse('view_shopping_cart'))
