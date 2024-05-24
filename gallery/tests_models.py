from django.test import TestCase
from .models import Gallery

class GalleryModelTest(TestCase):
    def setUp(self):
        self.gallery = Gallery.objects.create(
            name="Test Gallery",
            description="Test Description",
            gallery_image="test_image.jpg"
        )

    def test_gallery_attributes(self):
        """Test if Gallery attributes are correctly set"""
        self.assertEqual(self.gallery.name, "Test Gallery")
        self.assertEqual(self.gallery.description, "Test Description")
        self.assertEqual(self.gallery.gallery_image, "test_image.jpg")

    def test_string_representation(self):
        """Test string representation of Gallery"""
        self.assertEqual(str(self.gallery), "Test Gallery")