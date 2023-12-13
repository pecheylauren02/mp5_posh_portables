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

    # Handles the form submission process
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = author
            review.save()

            # Updates the product rating on the product object
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(is_approved=True).aggregate(
                        Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            messages.success(
                request,
                "Your review has been created. " +
                "It will appear on the site once it has been approved. " +
                "You can see your review on your profile page until then. " +
                "We value your feedback here at Posh Portables!"
            )

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Uh Oh! Looks like your form is invalid, please try again.")

    # Handles the View Rendering
    else:
        form = ReviewForm()

    # Sets the page template
    template = 'reviews/create_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)