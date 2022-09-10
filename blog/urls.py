from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('ratings/<slug:slug>', views.PostReviews.as_view(), name='post-review'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]