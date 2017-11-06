from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class SellItemInfo(models.Model): #never make the model and forms name same it will make u suffer much........(^_^)v

    uploader = models.ForeignKey(User, null=True, blank=True)
    item_name = models.CharField(max_length=25,blank=False)
    item_type = models.CharField(max_length=15,blank=False)
    item_location = models.TextField(blank=False)
    item_exprice = models.CharField(max_length=50,blank=False)
    item_usetime = models.CharField(max_length=15,blank=False)
    item_reason = models.TextField(blank=False)
    item_pic = models.ImageField(upload_to='useritems',blank=True)
