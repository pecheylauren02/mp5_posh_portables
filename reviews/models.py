from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)
from django.contrib.auth.models import User
from products.models import Product


class Reviews(models.Model):
    """
    A model that handles user reviews
    """
    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey(
            Product, on_delete=models.CASCADE,
            null=True, blank=True,
            related_name="reviews")

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews")

    title = models.CharField(
        max_length=40,
        blank=False,
        null=False
    )
    created_on = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
        default=0,
        blank=False,
        null=False
    )
    content = models.TextField(
        max_length=500
    )
    is_approved = models.BooleanField(
        default=False
    )

    def __str__(self):
        """
        Review title String conversion
        """
        return f"{self.title} by {self.user.username} for {self.product.name}"
