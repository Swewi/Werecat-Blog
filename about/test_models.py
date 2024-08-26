from django.test import TestCase
from django.urls import reverse
from .models import About

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About.objects.create(
            title="About Me",
            profile_image="path/to/image.jpg",  
            content="This is about me."
        )
