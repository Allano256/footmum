from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Broadcast(models.Model):
    """
    Broadcast model is related to owner.
    """
    image_choice_filter= [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    title =models.CharField(max_length=255)
    content=models.TextField(blank=True)
    image = models.ImageField(
        upload_to='image/', default='../bio/images/nobody.jpg', blank=True
    )
    image_filter=models.ImageField(
        max_length=32, choices=image_choice_filter, default='normal'
    )

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
