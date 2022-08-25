from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models 


class Bag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name 

class BagReview(models.Model):
    rating = models.ManyToManyField():

    
    
   











