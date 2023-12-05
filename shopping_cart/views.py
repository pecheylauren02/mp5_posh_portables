from django.shortcuts import render, redirect, reverse, HttpResponse

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
        shopping_cart.pop(item_id)

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_shopping_cart'))

def remove_from_shopping_cart(request, item_id):
    """ Remove the item from the shopping cart """
    try:
        shopping_cart = request.session.get('shopping_cart', {})
        shopping_cart.pop(item_id, None)
        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)
    except KeyError:
        return HttpResponse(status=404)
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse(status=500)

