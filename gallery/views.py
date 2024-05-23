from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Gallery

def gallery(request):
    
    """
    View function to render the gallery page with gallery items.
    """
    
    gallery_items_list = Gallery.objects.all()
    paginator = Paginator(gallery_items_list, 4)  # Show 4 gallery items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'gallery_items': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'gallery/gallery.html', context)
