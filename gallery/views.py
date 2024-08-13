from django.shortcuts import render
from .models import Gallery

def gallery(request):
    """
    View function to render the gallery page with all gallery items.
    """
    
    gallery_items = Gallery.objects.all()

    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'gallery/gallery.html', context)