from django.db import models
from cloudinary.models import CloudinaryField

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')  # Using CloudinaryField for storing images

    def __str__(self):
        return self.name


