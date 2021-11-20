from django.urls import path
from .views import (
    PostListView, 
    UserPostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView
    )
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name="blog-home"),
    path('blog/<str:username>/', UserPostListView.as_view(), name="blog-user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name="post-comment"),
    path('about/', views.about, name="blog-about"),
]