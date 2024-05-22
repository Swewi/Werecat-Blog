from django.shortcuts import render
from .models import Gallery

def gallery(request):
    gallery_items = Gallery.objects.all()
    cloudinary_img = {'gallery_items': gallery_items}
    return render(
        request,
        'gallery/gallery.html',
        cloudinary_img
    )