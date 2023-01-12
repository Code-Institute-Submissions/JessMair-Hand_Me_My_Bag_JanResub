""" Import and implementation of forms """
from django import forms
from .models import Comment


class CommentForm (forms.ModelForm):
    """
    Define comment form
    """
    class Meta:
        """
        The body and rating fields of comment form can be added to
        """
        model = Comment
        fields = ('body', 'rating')


class CommentUpdateForm (forms.ModelForm):
    """
    Define updating comment on the form
    """
    class Meta:
        """
        The body and rating fields can be edited bu user
        """
        model = Comment
        fields = ('body', 'rating')
