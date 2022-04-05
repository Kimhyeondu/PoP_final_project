from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# Create your models here.


class User(AbstractUser):
    class Meta:
        db_table = "user"

    profile_img = models.ImageField(upload_to='avatar/',)
    tag = TaggableManager(blank=True)
    bio = models.CharField(max_length=256, default='')