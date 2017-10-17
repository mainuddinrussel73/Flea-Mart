from django.db import models

class UserDetails(models.Model):
    user_name = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=10)

    def __str___(self):
            return self.user_name

class userHome(models.Model):
    user_name = models.ForeignKey(UserDetails)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=25)
    url = models.URLField()
    def __str___(self):
        return self.user_name+password
# Create your models here.
