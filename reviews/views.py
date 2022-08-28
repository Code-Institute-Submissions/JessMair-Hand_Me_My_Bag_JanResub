from django.shortcuts import render

from .models import Review, Bag

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.all(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class review_list(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostReview(View):

    def get(self, request, *args, **kwards):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)
        reviewed = False
        if post.reviewed.filter:
            reviewed = True


    def review_detail(request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        return render(request, 'reviews/review_detail.html', {'review': review})            

