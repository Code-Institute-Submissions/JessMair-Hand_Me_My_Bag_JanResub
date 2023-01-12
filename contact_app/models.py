""" All models for the Contact app """
from django.db import models


class Contact(models.Model):
    """ Model for the contact us form """
    name = models.CharField(max_length=158, blank=False)
    email = models.EmailField(blank=False, default='')
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
