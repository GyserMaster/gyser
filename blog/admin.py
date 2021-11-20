from django.contrib import admin
from .models import Post, Comment


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('post', ('date_comment', 'name', 'email'), 'comment')
    date_hierarchy = 'date_comment'
    list_filter = ('post', 'email', 'name')
    search_fields = ['comment']
