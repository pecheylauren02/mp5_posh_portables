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


@login_required()
def create_faq(request):
    """
    For users to create FAQs.
    Only the Admin can access it.
    Adds new FAQs to the database.
    """

    # Checks if the user is admin
    # redirects to faqs page if not
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add FAQs.')
        return redirect(reverse('faqs'))

    # Handles Form Submission
    if request.method == "POST":
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()

            request.session['show_bag_summary'] = False
            messages.success(request, "New FAQ added.")
            return redirect(reverse('faqs'))
        else:
            messages.error(request, "Oops. Your form invalid," + " "
                           "please check that you have filled it in correctly.")