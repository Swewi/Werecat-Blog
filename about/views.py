from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.

def about_us(request):
    
    """
    View function to render the about page with about us information.
    """
    
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )