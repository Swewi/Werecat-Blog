from django.test import TestCase
from unittest.mock import patch
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

    def test_gallery_image_accepts_none(self):
        """Test that gallery_image can be None"""
        gallery = Gallery.objects.create(
            name="Test Gallery",
            description="Test Description",
            gallery_image=None
        )
        self.assertIsNone(gallery.gallery_image)

    def test_save_gallery(self):
        """Test that a gallery object is saved correctly"""
        gallery = Gallery(
            name="Another Test Gallery",
            description="Another Test Description",
            gallery_image="another_test_image.jpg"
        )
        gallery.save()
        self.assertEqual(Gallery.objects.count(), 2)