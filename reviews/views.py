from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Reviews
from .forms import ReviewForm
from products.models import Product


@login_required()
def create_review(request, product_id):
    """
    Renders the form for logged in only users 
    to write a review for a product.
    Adds the new review to the database.
    """

    # Sets product variable to the product_id
    product = get_object_or_404(Product, pk=product_id)

    # Sets the author as the logged in user
    author = User.objects.get(username=request.user)
