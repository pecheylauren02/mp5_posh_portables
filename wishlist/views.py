from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WishlistItem


@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    # Implement logic to add a product to the user's wishlist
    # Ensure that the user is authenticated and handle duplicates if needed
    return redirect('wishlist')
    
@login_required
def remove_from_wishlist(request, item_id):
    # Implement logic to remove a product from the user's wishlist
    # Ensure that the user is authenticated
    return redirect('wishlist')