from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=64)
    body = models.TextField()
    created_on = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
