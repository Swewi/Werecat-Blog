from django.shortcuts import render
from .models import Gallery

# Create your views here.

def gallery(request):
    # Fetch all instances of the Gallery model
    items = Gallery.objects.all()
    
    return render(
        request,
        'gallery/gallery.html',
        {'gallery_items': gallery_items},
    )