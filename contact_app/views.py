from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.subject = subject
        contact.message = message
        contact.save()
        
    return render(request, 'contact.html')