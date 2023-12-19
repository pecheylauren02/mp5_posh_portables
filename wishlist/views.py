from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishlistItem, Product


@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html',
                  {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request, product_id):
    """ Adds product to user's wishlist """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        WishlistItem.objects.create(user=request.user, product=product)

        messages.success(request, f'{product.name} added to your wishlist!')

    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    """ Deletes product from user's wishlist """
    # Ensure that the user is authenticated
    user = request.user

    # Get the wishlist item or return a 404 response if not found
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=user)

    # Delete the wishlist item
    wishlist_item.delete()

    # Redirect to the wishlist page
    return redirect('wishlist')
