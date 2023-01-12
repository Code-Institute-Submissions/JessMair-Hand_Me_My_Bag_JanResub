from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('<pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
