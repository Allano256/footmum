from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Bio(models.Model):
    """
    This model will create the user's profile, with an image and content field. It will also save the profile.
    """
    owner=models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField( max_length=50, default='')
    created_at =models.DateTimeField(  auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/', blank=True,
                  default='../bio/images/nobody.jpg')
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return f"{self.owner}'s"
    
    def create_profile(sender,instance, created, **kwargs):
        if created:
            Bio.objects.create(owner=instance)

    post_save.connect(create_profile, sender=User)
