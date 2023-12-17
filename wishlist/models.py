from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    """
    A model to create wishlists for users
    Will be linked directly with products
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist Item: {self.product.name}"

