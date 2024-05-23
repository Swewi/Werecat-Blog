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

    def test_about_view(self):
        """Test the about view."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.about_content.title)
        self.assertContains(response, self.about_content.content)