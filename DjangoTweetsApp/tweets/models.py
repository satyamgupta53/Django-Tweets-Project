from django.db import models
from django.contrib.auth.models import User # User model from django.contrib.auth.models

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey to User model
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:40]}'