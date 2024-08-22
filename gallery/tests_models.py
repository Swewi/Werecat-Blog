from django.test import TestCase
from unittest.mock import patch
from .models import Gallery

@patch('cloudinary.uploader.upload')
def test_gallery_image_field(self, mock_upload):
    """Test that gallery_image field accepts valid image data"""
    mock_upload.return_value = {'url': 'http://example.com/valid_image.jpg'}
    valid_image = 'valid_image.jpg'
    gallery = Gallery.objects.create(
        name="Test Gallery",
        description="Test Description",
        gallery_image=valid_image
    )
    self.assertEqual(gallery.gallery_image.url, 'http://example.com/valid_image.jpg')

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