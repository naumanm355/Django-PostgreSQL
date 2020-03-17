from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name="blog"),
    path('posts', views.post, name="post"),
    path('insert', views.insert_blog_item, name="insertitem"),
    path('insertpo', views.insert_post_item, name="insertpost"),
    path('geteditpost/<int:postId>/',
         views.get_editpost_item, name="get_editpost"),
    path('updatepost/<int:postId>/', views.updatepost, name="updatepost"),
    path('deletepost/<int:postId>/', views.deletepost, name="delete_post"),
    path('geteditblog/<int:blogId>/',
         views.get_editblog_item, name="get_editblog"),
    path('updateblog/<int:blogId>/', views.updateblog, name="updateblog"),
    path('deleteblog/<int:blogId>/', views.deleteblog, name="delete_blog"),

]
