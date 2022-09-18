from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm, CommentUpdate, CommentUpdateForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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

    def post(self, request, slug, *args, **kwargs):
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
            },
        )


    #def update_comment(request, id):
        #comment = get_object_or_404(Comment, id=id)
       # form = CommentUpdateForm(request.POST or None, instance=comment)
        #if request.user != comment.author:
            #return redirect('post_list')
            #if form.is_valid():
            #    form.save()
 
            #return redirect('post_list')

          #  return render(request,'comment/post_detal.html', {'form': form})


#class CommentUpdate(LoginRequiredMixin, UpdateView):
    #model = CommentForm
   # fields = ['name', 'body', 'rating']
   # template_name = 'post_detail'
   # get_success_url = 'comment.id'

    
    #def get (self, user, form):
        #self.object = self.get_object_or_404()
        #form.instance.author = self.request.user
        #return super().get(request, *args, **kwargs)


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = CommentForm 
    success_url = reverse_lazy()
    template_name = 'post_detail.html'



class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
