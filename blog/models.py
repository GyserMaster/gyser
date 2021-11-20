from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(config_name='custom_one',blank=True,null=True,external_plugin_resources=[('youtube', '/static/static/blog/ckeditor_plugins/youtube/', 'plugin.js')]) # RichTextField(config_name='awesome_ckeditor')
    # ,external_plugin_resources=[('yt', '/static/static/ckeditor/ckeditor/plugins/youtube/youtube/', 'plugin.js')] /static/static/ckeditor/ckeditor/plugins/youtube/ /static/static/blog/ckeditor_plugins/youtube/
    #static/static/ckeditor/ckeditor/plugins/youtube/youtube
    date_posted = models.DateTimeField(default=timezone.now) # models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
        

class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=True, null=True)
    comment = RichTextUploadingField(config_name='custom_two', blank=True,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comments')
    date_comment = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.post}'