from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faq
from .forms import FaqForm


def faqs(request):
    """
    A view to return the FAQs
    """

    # Gets faqs from DB
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)


@login_required()
def create_faq(request):
    """
    Renders form to create FAQ.
    Admin only can access this.
    Adds new faq to database.
    """

    # Checks user is admin
    # redirects to faqs if not
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can create FAQs.')
        return redirect(reverse('faqs'))

    # Handles Form Submission
    if request.method == "POST":
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "New FAQ added.")
            return redirect(reverse('faqs'))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = FaqForm()

    # Sets page template
    template = 'faqs/add_faq.html'

    # Sets current faq & form content
    context = {
        'form': form,
    }

    return render(request, template, context)
