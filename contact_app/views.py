""" View file for the contact app """
from django.shortcuts import render
from .models import Contact


def index(request):
    """
    Direct view to render instruction held in the index template
    """
    return render(request, 'index.html')


def contact(request):
    """
    View of contact form
    """
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'contact.html')
