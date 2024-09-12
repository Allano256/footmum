from django.db import models
from django.contrib.auth.models import User

from post.models import Broadcast

# Create your models here.

class Likes(models.Model):
    """
    This model is related to owner and broadcast, using the unique_together ensures that a user cant like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    broadcast = models.ForeignKey(Broadcast, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering= ['-created_at']
        unique_together = ['owner','broadcast']

    def __str__(self):
        return f'{self.owner} {self.broadcast}'
