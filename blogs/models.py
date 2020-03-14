from django.db import models

# Create your models here.


class Blog(models.Model):
    uid = models.AutoField(primary_key=True, blank=False)
    apiname = models.CharField(max_length=50, unique=True, blank=False)
    display_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


class Post(models.Model):
    uid = models.AutoField(primary_key=True, blank=False)
    apiname = models.CharField(max_length=50, unique=True, blank=False)
    display_name = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
