from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def handler404(request, exception):
    """ 
    Error Handler 404 - Page Not Found 
    """
    return render(request, "errors/404.html", status=404)