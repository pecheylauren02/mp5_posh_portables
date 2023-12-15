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
def create_reviews(request, product_id):
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
            review.is_approved = False
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
            print(form.errors)
            messages.error(request, "Uh Oh! Looks like your form is invalid, please try again.")

    # Handles the View Rendering
    else:
        form = ReviewForm()

    # Sets the page template
    template = 'reviews/create_reviews.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def update_review(request, review_id):
    """
    Renders form to update the review.
    Logged in Users Only (redirects to log in).
    Updates review on database.
    """

    review = get_object_or_404(Reviews, pk=review_id)
    product = Product.objects.filter(reviews=review)[0]

    # Checks user is author of review
    # redirects to product detail if not
    if request.user != review.user:
        messages.error(request, 'You can only update your own reviews.')
        return redirect(reverse('product_detail', args=[product.id]))

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save()
            review.is_approved = False
            review.save()

            # Gets URL to redirect user back to previous page
            redirect_url = request.POST.get('redirect_url', reverse('product_detail', args=[product.id]))

            # Updates product rating on product object
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(
                        is_approved=True).aggregate(
                            Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            messages.success(
                request,
                "Your review has been updated. " +
                "It will appear on the site once it has been approved. " +
                "You can see your review on your profile page until then."
            )
            return redirect(redirect_url)
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing... "{review.title}"')

    # Sets page template
    template = 'reviews/update_reviews.html'

    # Sets current product & form content
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def remove_review(request, review_id):
    """
    Removes a review from the database.
    Only the author of the review can remove it.
    """

    # Get the review object
    review = get_object_or_404(Reviews, pk=review_id)
    product = Product.objects.filter(reviews=review).first()

    # Check if the logged-in user is the author of the review
    if request.user != review.user:
        messages.error(request, 'You can only remove your own reviews.')
        return redirect(reverse('product_detail', args=[product.id]))

    # Remove the review from the database
    review.delete()

    # Update product rating on product object
    if product.reviews.filter(is_approved=True).count() > 0:
        product.rating = round(
            product.reviews.filter(
                is_approved=True).aggregate(
                    Avg('rating'))['rating__avg'])
    else:
        product.rating = 0
    product.save()

    messages.success(request, "Your review has been removed.")

    # Redirect back to the product detail page
    return redirect(reverse('product_detail', args=[product.id]))
