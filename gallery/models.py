from django.db import models
from cloudinary.models import CloudinaryField

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    gallery_image = CloudinaryField('image')

    def __str__(self):
        return self.name


