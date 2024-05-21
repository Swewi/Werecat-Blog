from django.contrib import admin
from .models import Gallery
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)