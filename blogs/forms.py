from django import forms
from .models import Blog, Post

# Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['apiname', 'display_name', 'author']


class searchBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['apiname', 'display_name', 'author']


# Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['apiname', 'display_name', 'content']
