from django.shortcuts import render


def post(request):
    return render(request, "posts.html", {})


def blog(request):
    return render(request, "blogs.html", {})
