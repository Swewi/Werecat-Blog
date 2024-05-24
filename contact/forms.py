from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Message'
        }