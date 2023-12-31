from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from reviews.models import Reviews
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Displays the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile updated successfully')
        else:
            messages.error(request, 'Oops. The update failed. \
                           Please fill in the form correctly.')

    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Get user reviews
    user_reviews = Reviews.objects.filter(user=request.user, is_approved=True)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_reviews': user_reviews,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Displays the user's order history """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
