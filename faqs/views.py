from django.shortcuts import render


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