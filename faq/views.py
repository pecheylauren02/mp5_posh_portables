from django.shortcuts import render

def faq(request):
    # Your view logic here
    return render(request, 'faq/faq.html')  # Adjust the template path as needed