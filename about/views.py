from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.

def about_us(request):
    """
    Renders the most recent information about the website author.
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )