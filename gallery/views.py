from django.shortcuts import render
from .models import Gallery

def gallery(request):
    # Fetch all instances of the Gallery model
    gallery_items = Gallery.objects.all()
    
    return render(
        request,
        'gallery/gallery.html',
        {'gallery_items': gallery_items},
    )