from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Contact

class ContactModelTest(TestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(
            name="John Doe",
            email="john@example.com",
            message="Hello, this is a test message."
        )
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "john@example.com")
        self.assertEqual(contact.message, "Hello, this is a test message.")
        self.assertFalse(contact.read)

    def test_str_representation(self):
        contact = Contact(name="Jane Doe", email="jane@example.com")
        self.assertEqual(str(contact), "Jane Doe")

    def test_blank_name_and_message(self):
        contact = Contact.objects.create(email="test@example.com")
        self.assertEqual(contact.name, "")
        self.assertEqual(contact.message, "")

    def test_email_validation(self):
        with self.assertRaises(ValidationError):
            contact = Contact(email="invalid-email")
            contact.full_clean()

    def test_default_read_status(self):
        contact = Contact.objects.create(email="test@example.com")
        self.assertFalse(contact.read)

    def test_update_read_status(self):
        contact = Contact.objects.create(email="test@example.com")
        contact.read = True
        contact.save()
        self.assertTrue(Contact.objects.get(id=contact.id).read)