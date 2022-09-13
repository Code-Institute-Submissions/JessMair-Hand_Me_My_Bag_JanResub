from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=158)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name