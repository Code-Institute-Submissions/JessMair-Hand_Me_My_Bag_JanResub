""" Configuration pf apps """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration of the blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
