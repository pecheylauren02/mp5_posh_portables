from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import WishlistItem, Product

class TestWishlistViews(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        # Create a product
        self.product = Product.objects.create(
            name='Gaming Laptop',
            description='Gaming Laptop Description',
            price=10.99
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a WishlistItem
        self.wishlist_item = WishlistItem.objects.create(
            user=self.user,
            product=self.product
        )

    def test_wishlist_view(self):
        response = self.client.get(reverse('wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_add_to_wishlist_view(self):
        response = self.client.post(reverse('add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('wishlist'))
        self.assertTrue(WishlistItem.objects.filter(user=self.user, product=self.product).exists())

    def test_remove_from_wishlist_view(self):
        response = self.client.post(reverse('remove_from_wishlist', args=[self.wishlist_item.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('wishlist'))
        self.assertFalse(WishlistItem.objects.filter(id=self.wishlist_item.id).exists())
