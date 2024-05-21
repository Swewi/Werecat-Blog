from django.contrib import admin
from .models import Gallery
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']