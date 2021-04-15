from django.urls import path
from blog import views as blog_views


urlblog = [
    path('blog/', blog_views.blog, name="blog")
]