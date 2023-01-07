""" Here are two Django models. 'Post' and 'Comment' """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """ This is Django model for the blog post """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    description = models.TextField(null=True)

    class Meta:
        """ This orders the posts based on when they were created.
        The newest posts will be at the top """
        ordering = ['-created_on']

    def __str__(self):
        """ Returns title field of post as a string """
        return self.title

    def number_of_likes(self):
        """ Counts and displays the number of likes post has received """
        return self.likes.count()


class Comment(models.Model):
    """" Django comment model, with a ratings field to act as a significant
    customisation of the model """

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=3,)

    def get_absolute_url(self):
        """ Custom model to return URL which redirects user to detail page
        of the comment """
        return reverse('comment-detail', kwargs={'pk': self.pk})
