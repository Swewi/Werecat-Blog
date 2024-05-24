from django.test import TestCase
from django.urls import reverse
from .models import Gallery

class TestGalleryView(TestCase):

    def setUp(self):
        # Create 10 gallery items for pagination testing
        for i in range(10):
            Gallery.objects.create(name=f"Item {i}", gallery_image=f"image_{i}.jpg", description=f"Description for item {i}")

    def test_gallery_view_status_code(self):
        """Test if the gallery view returns a 200 status code"""
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        """Test if the gallery view uses the correct template"""
        response = self.client.get(reverse('gallery'))
        self.assertTemplateUsed(response, 'gallery/gallery.html')

    def test_gallery_view_pagination(self):
        """Test if pagination is enabled and controls are present"""
        response = self.client.get(reverse('gallery'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertTrue(response.context['page_obj'].has_other_pages())  # Check if there are other pages

    def test_gallery_view_context(self):
        """Test if the context contains the expected keys"""
        response = self.client.get(reverse('gallery'))
        self.assertTrue('gallery_items' in response.context)
        self.assertTrue('page_obj' in response.context)

    def test_gallery_view_items(self):
        """Test if gallery items are displayed correctly"""
        response = self.client.get(reverse('gallery'))
        # Check that the first 4 items are in the first page
        for i in range(4):
            self.assertContains(response, f"Item {i}")
            self.assertContains(response, f"Description for item {i}")
        
        # Check that at least one item is on the next page
        response = self.client.get(reverse('gallery') + '?page=2')
        self.assertContains(response, "Item 4")
        self.assertContains(response, "Description for item 4")

    def test_gallery_view_image_urls(self):
        """Test if gallery items' images are displayed using Cloudinary URLs"""
        response = self.client.get(reverse('gallery'))
        for i in range(4):
            self.assertContains(response, f"src=\"{self.get_cloudinary_url(f'image_{i}.jpg')}\"")

    def get_cloudinary_url(self, image_name):
        """Helper function to get the Cloudinary URL for a given image name"""
        from cloudinary.utils import cloudinary_url
        url, _ = cloudinary_url(image_name)
        return url