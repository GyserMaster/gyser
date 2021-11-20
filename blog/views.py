from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = "blog/testing.html" # DEFAULT <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html" # DEFAULT <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post  
    context_object_name = 'post' # en el template-tag utiliza 'post' u 'object'
    template_name = "blog/post_detail.html" # DEFAULT <app>/<model>_<viewtype>.html
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/post_form.html"
    success_message = 'Comment successfully created!'
    error_message = 'Error saving the comment, check fields below.'


    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        messages.success(self.request, self.success_message)
        #form.instance.user = self.request.user # if you want to ignore the post field, you can put null=True in the Comment Model:
        return super(CommentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self, **kwargs):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html" # DEFAULT <app>/<model>_<viewtype>.html
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html" # DEFAULT <app>/<model>_<viewtype>.html
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Testing'
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/testing.html', context)

def about(request):
    form = PostForm()
    context = {
        'title': 'About',
        'form': form
    }
    #return HttpResponse('<h1>About Home Page</h1>')
    return render(request, 'blog/about.html', {'form': form})


def comment(request):
    form = CommentForm()
    context = {
        'title': 'Comment',
        'form': form
    }
    #return HttpResponse('<h1>About Home Page</h1>')
    return render(request, 'blog/about.html', {'form': form})