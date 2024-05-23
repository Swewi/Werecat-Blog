from django.test import TestCase
from django.urls import reverse
from .models import About

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About.objects.create(
            title="About Me",
            content="This is about me."
        )

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertContains(response, self.about_content.title)
        self.assertContains(response, self.about_content.content)