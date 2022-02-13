from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    username = models.CharField(max_length=250)
    content = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  null=True, blank=True)
