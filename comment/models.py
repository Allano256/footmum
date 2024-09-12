from django.db import models
from django.contrib.auth.models import User
from  post.models import Broadcast

# Create your models here.


class Comment(models.Model):
    """
    This is related to a User an Post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering=['-created_at']


    def __str__(self):
        return {self.content}


