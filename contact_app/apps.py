""" Model configuration """
from django.apps import AppConfig


class ContactAppConfig(AppConfig):
    """ Contact model configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_app'
