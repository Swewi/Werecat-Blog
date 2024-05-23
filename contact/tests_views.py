from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import ContactForm

class TestContactView(TestCase):

    def test_render_contact_page_with_contact_form(self):
        """Verifies get request for contact page containing a contact form"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'We love crafting!', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactForm)

    def test_successful_contact_submission(self):
        """Test for a user submitting a contact form"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('contact'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Hi I have received your message! I will do my best to respond within 2 working days.', response.content)