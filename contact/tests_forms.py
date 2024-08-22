from django.test import TestCase
from django.core.exceptions import ValidationError
from django import forms
from .forms import ContactForm

class TestContactForm(TestCase):
    
    def test_form_fields(self):
        """Test that the form has only the expected fields"""
        form = ContactForm()
        expected_fields = ['name', 'email', 'message']
        self.assertSequenceEqual(list(form.fields.keys()), expected_fields)

    def test_form_is_valid(self):
        """Test for all fields with valid data"""
        form = ContactForm({
            'name': 'Test Name',
            'email': 'test@example.com',
            'message': 'Hello, this is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_name_field(self):
        """Test the 'name' field"""
        form = ContactForm({'name': '', 'email': 'test@example.com', 'message': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'name', 'This field is required.')

        long_name = 'a' * 201
        form = ContactForm({'name': long_name, 'email': 'test@example.com', 'message': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'name', 'Ensure this value has at most 200 characters (it has 201).')

    def test_email_field(self):
        """Test the 'email' field"""
        form = ContactForm({'name': 'Test', 'email': '', 'message': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'email', 'This field is required.')

        form = ContactForm({'name': 'Test', 'email': 'invalid-email', 'message': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'email', 'Enter a valid email address.')

    def test_message_field(self):
        """Test the 'message' field"""
        form = ContactForm({'name': 'Test', 'email': 'test@example.com', 'message': ''})
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'message', 'This field is required.')

        self.assertIsInstance(form.fields['message'].widget, forms.Textarea)

    def test_form_widgets(self):
        """Test that the correct widgets are being used"""
        form = ContactForm()
        self.assertIsInstance(form.fields['name'].widget, forms.TextInput)
        self.assertIsInstance(form.fields['email'].widget, forms.EmailInput)
        self.assertIsInstance(form.fields['message'].widget, forms.Textarea)