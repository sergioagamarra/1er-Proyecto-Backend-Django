from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    img = models.CharField(max_length=240)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " - " + self.title

    def get_url(self):
        return reverse('posts:post_detail', args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)


