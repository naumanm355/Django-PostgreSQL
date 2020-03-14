from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('posts', views.post, name="post"),
    path('insert', views.insert_blog_item, name="insertitem"),
    path('insertpo', views.insert_post_item, name="insertpost")
]
