from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# Create your models here.


class User(AbstractUser):
    LOGIN_EMAIL = 'email'
    LOGIN_KAKAO = 'kakao'
    LOGIN_CHOICES = ((LOGIN_EMAIL,'Email'),(LOGIN_KAKAO, 'Kakao'))
    login_method = models.CharField(choices=LOGIN_CHOICES, max_length=20, default=LOGIN_EMAIL)
    profile_img = models.ImageField(upload_to='profile_img/')
    tag = TaggableManager(blank=True)
    
    def __str__(self):
        return self.username