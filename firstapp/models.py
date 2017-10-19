from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portfolio = models.URLField(blank=True)
    profilepic = models.ImageField(upload_to='profilepics',blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
