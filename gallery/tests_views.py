from django.test import TestCase
from django.urls import reverse
from .models import Gallery

class TestGalleryView(TestCase):
    def test_gallery_view_status_code(self):
        """Test if the gallery view returns a 200 status code"""
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        """Test if the gallery view uses the correct template"""
        response = self.client.get(reverse('gallery'))
        self.assertTemplateUsed(response, 'gallery/gallery.html')

    def test_gallery_view_context(self):
        """Test if the context contains the expected keys"""
        response = self.client.get(reverse('gallery'))
        self.assertIn('gallery_items', response.context)

    def test_gallery_view_items(self):
        """Test if gallery items are displayed correctly"""
        # Create some test gallery items
        for i in range(3):
            Gallery.objects.create(
                name=f"Item {i}",
                description=f"Description for item {i}",
                gallery_image=f"image_{i}.jpg"
            )
       
        response = self.client.get(reverse('gallery'))
       
        # Check that all items are in the response
        for i in range(3):
            self.assertContains(response, f"Item {i}")
            self.assertContains(response, f"Description for item {i}")

    def test_gallery_view_image_urls(self):
        """Test if gallery items' images are present in the response"""
        # Create some test gallery items
        for i in range(3):
            Gallery.objects.create(
                name=f"Item {i}",
                description=f"Description for item {i}",
                gallery_image=f"image_{i}.jpg"
            )
       
        response = self.client.get(reverse('gallery'))
       
        for i in range(3):
            self.assertContains(response, f"image_{i}.jpg")