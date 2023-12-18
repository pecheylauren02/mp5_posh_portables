from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import WishlistItem

class TestWishlistItemModel(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.99
        )

        # Create a WishlistItem
        self.wishlist_item = WishlistItem.objects.create(
            user=self.user,
            product=self.product
        )

    def test_wishlist_item_str(self):
        """
        Test the __str__ method of WishlistItem model
        """
        expected_str = f"{self.user.username}'s Wishlist Item: {self.product.name}"
        self.assertEqual(str(self.wishlist_item), expected_str)

    def test_wishlist_item_user_relationship(self):
        """
        Test the relationship between WishlistItem and User
        """
        self.assertEqual(self.wishlist_item.user, self.user)

    def test_wishlist_item_product_relationship(self):
        """
        Test the relationship between WishlistItem and Product
        """
        self.assertEqual(self.wishlist_item.product, self.product)

    def test_wishlist_item_deletion(self):
        """
        Test that the WishlistItem is deleted when related User is deleted
        """
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(WishlistItem.DoesNotExist):
            WishlistItem.objects.get(user_id=user_id)
