from django.shortcuts import render, redirect
from django.http import HttpRequest
from . models import Blog, Post
from .forms import searchBlog
# Create your views here.


def blog(request):
    context = {
        'blogList': Blog.objects.all(),
        form: searchBlog(request.POST or None)
    }
    return render(request, "blogs.html", context)


def insert_blog_item(request: HttpRequest):
    blogg = Blog()
    blogg.apiname = request.POST.get('apiname')
    blogg.display_name = request.POST.get('dispname')
    blogg.author = request.POST.get('author')
    blogg.save()
    return redirect('blog')


def post(request):
    context = {'postList': Post.objects.all()}
    return render(request, "posts.html", context)


def insert_post_item(request: HttpRequest):
    postt = Post()
    postt.apiname = request.POST.get('apiname')
    postt.display_name = request.POST.get('dispname')
    postt.content = request.POST.get('content')
    postt.save()
    return redirect('post')
