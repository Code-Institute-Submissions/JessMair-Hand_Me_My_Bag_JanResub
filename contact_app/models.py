from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=158, blank=False)
    email = models.EmailField(blank=False, default='')
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name