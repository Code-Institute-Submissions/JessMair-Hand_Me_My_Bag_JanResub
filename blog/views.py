""" This is a view for the blog which is an app of the site.
Class-based views have been used """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """ This class is to display a list of blog posts """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """ This is a view to display the details of the blog post.
    This function will retrieve all approved data from the database."""
    def get(self, request, slug):
        """ This function uses the GET method and handles HTTP GET requests """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        """ Using the POST method to handle HTTP POST requests """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class CommentUpdate(LoginRequiredMixin, UpdateView):
    """ This view will handle updating comments """
    model = Comment
    form_class = CommentForm
    template_name = 'update.html'
    success_url = reverse_lazy("home")

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )


class CommentDelete(LoginRequiredMixin, DeleteView):
    """ This view takes care of deleting a comment """
    model = Comment
    template_name = 'delete.html'
    success_url = reverse_lazy("home")

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )


class PostLike(View):
    """ This view handles 'liking' and 'unliking' a blog post """
    def post(self, request, slug):
        """ Here the POST method is being used """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
