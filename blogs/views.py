from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
# ,HttpResponse
from django.db.models import Q
from . models import Blog, Post
from .forms import searchBlog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# create blog view and show all data of blog here


def blog(request):
    ctx = {}
    searchParameter = request.GET.get("search")
    if searchParameter:
        blogList = Blog.objects.filter(
            Q(apiname__icontains=searchParameter) | Q(author__icontains=searchParameter) | Q(uid__icontains=searchParameter) | Q(display_name__icontains=searchParameter))
    else:
        blogList = Blog.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(blogList, 10)
        try:
            blogList = paginator.page(page)
        except PageNotAnInteger:
            blogList = paginator.page(1)
        except EmptyPage:
            blogList = paginator.page(paginator.num_pages)
    ctx["blogList"] = blogList
    return render(request, "blogs.html", context=ctx)
    # context = {
    #     'blogList': Blog.objects.all(),
    #     # form: searchBlog(request.POST or None)
    # }


# insert data into blog model


def insert_blog_item(request: HttpRequest):
    blogg = Blog()
    blogg.apiname = request.POST.get('apiname')
    blogg.display_name = request.POST.get('dispname')
    blogg.author = request.POST.get('author')
    blogg.save()
    return redirect('blog')

# create post view and show all data of Post here


def post(request):
    ctx = {}
    searchParameter = request.GET.get('search')
    if searchParameter:
        postList = Post.objects.filter(
            Q(apiname__icontains=searchParameter) | Q(uid__icontains=searchParameter) | Q(display_name__icontains=searchParameter) | Q(content__icontains=searchParameter))
    else:
        postList = Post.objects.all()
    ctx["postList"] = postList
    return render(request, "posts.html", context=ctx)
    # context = {'postList': Post.objects.all()}
    # return render(request, "posts.html", context)

# insert data into post models


def insert_post_item(request: HttpRequest):
    postt = Post()
    postt.apiname = request.POST.get('apiname')
    postt.display_name = request.POST.get('dispname')
    postt.content = request.POST.get('content')
    postt.save()
    return redirect('post')

# get id of post item which is to be edited


def get_editpost_item(request, postId):

    post = Post.objects.get(pk=postId)

    return HttpResponse(post)
    # render(request,'editModal.html',{'editingPost':post})

# here is view of update post


def updatepost(request, postId):
    updatedPost = Post.objects.get(pk=postId)
    updatedPost.apiname = request.POST.get('apiname')
    updatedPost.display_name = request.POST.get('dispname')
    updatedPost.content = request.POST.get('content')
    updatedPost.save()
    return redirect('post')

# view of delete post


def deletepost(request, postId):
    deletepost = Post.objects.get(pk=postId)
    deletepost.delete()
    return redirect('post')

# here blog item is edited


def get_editblog_item(request, blogId):

    blog = Blog.objects.get(pk=blogId)

    return HttpResponse(blog)

# here is view of blog which is updating the blog


def updateblog(request, blogId):
    updatedPost = Blog.objects.get(pk=blogId)
    updatedPost.apiname = request.POST.get('apiname')
    updatedPost.display_name = request.POST.get('dispname')
    updatedPost.author = request.POST.get('author')
    updatedPost.save()
    return redirect('blog')

# deleting the blog


def deleteblog(request, blogId):
    deleteBlog = Blog.objects.get(pk=blogId)
    deleteBlog.delete()
    return redirect('blog')


def multi_deleteblog(request, selectedblogs):
    if selectedblogs == 'checkedAll':
        Blog.objects.all().delete()
    else:
        selected = [int(x) for x in selectedblogs.split(',')]
        for blogId in selected:
            Blog.objects.get(pk=blogId).delete()
    return redirect('blog')


def multi_deletepost(request, selectedposts):
    if selectedposts == 'checkedAll':
        Post.objects.all().delete()
    else:
        selected = [int(x) for x in selectedposts.split(',')]
        for postId in selected:
            Post.objects.get(pk=postId).delete()
    return redirect('post')
