""" To import or register models for admin panel """
from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
