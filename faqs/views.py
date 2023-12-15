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
    template = 'faqs/create_faq.html'

    # Sets current faq & form content
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_faq(request, faq_id):
    """ 
    View allows admin and superusers
    To edit and update their FAQs
    """

    # Checks user is superuser
    # redirects to FAQS if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only administrators can update FAQS.')
        return redirect(reverse('faqs'))

    # Get faq from DB
    faq = get_object_or_404(Faq, pk=faq_id)

    # Handle Form Submission
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)

        if form.is_valid():
            form.save()

            messages.success(request, 'Successfully updated FAQ!')

            # Redirects to 'faqs'
            return redirect(reverse('faqs'))

        else:
            messages.error(
                request, 'Failed to update FAQ. Please check the form.')

    # Handles View Rendering
    else:
        form = FaqForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    # Sets page template
    template = 'faqs/update_faq.html'

    # Sets current faq & form content
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)
