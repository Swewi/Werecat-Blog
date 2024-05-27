from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """
    View function to render the contact page with contact information.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Hi, I have received your message! I will do my best to respond within 2 working days.'
            )
            return redirect('contact')  # Redirect to the same page or another view to avoid form resubmission
    else:
        contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form},
    )