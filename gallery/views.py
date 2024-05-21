from django.shortcuts import render
from .models import Gallery

def gallery(request):
    gallery_items = Gallery.objects.all()
    return render(
        request,
        'gallery/gallery.html',
        {'gallery_items': gallery_items}
    )