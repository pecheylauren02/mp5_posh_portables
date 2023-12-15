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