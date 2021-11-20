from django import forms
from .models import Post, Comment
from captcha.fields import ReCaptchaField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):

    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', 'captcha']
        widgets = {'post' : forms.HiddenInput()}