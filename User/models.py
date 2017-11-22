from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
import string

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class CommentsManager(models.Manager):
    def filter_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentsManager,self).filter(content_type=content_type,object_id=obj_id)
        return qs

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    to = models.CharField(max_length=20)
    fromm =  models.CharField(max_length=20)
    message = models.CharField(max_length=200,null=True)

    def __unicode__(self):
        return self.message

class Notification(models.Model):
    count = models.CharField(max_length=20,null=True)
    to = models.CharField(max_length=20)
    fromm =  models.CharField(max_length=20)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.count)
    def __unicode__(self):
        return self.to
    def natural_key(self):
        return (self.to)
    def get_description(self):
        return self.description

class SellItemInfo(models.Model): #never make the model and forms name same it will make u suffer much........(^_^)v

    slug = models.SlugField(unique=True);
    uploader = models.ForeignKey(User, null=True, blank=True)
    item_name = models.CharField(max_length=25,blank=False)
    item_type = models.CharField(max_length=15,blank=False)
    item_location = models.TextField(blank=False)
    item_exprice = models.CharField(max_length=50,blank=False)
    item_usetime = models.CharField(max_length=15,blank=False)
    item_reason = models.TextField(blank=False)
    item_pic = models.ImageField(upload_to='useritems',blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='item_likes')
    likecount = models.IntegerField(default=0);
    def __str__(self):
        return str(self.slug)
    def get_slug(self):
        return self.slug
    def get_absolute_url(self):
        return reverse("User:details",kwargs={"slug":self.slug})
    # def get_like_url(self):
    #     return reverse("User:like-toggle", kwargs={"slug": self.slug})
    def get_api_like_url(self):
        return reverse("User:likes-api-toggle", kwargs={"slug": self.slug})
        # return "/details/%s/" %(self.id)
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    @property
    def contents(self):
        instance = self
        qs = Comments.objects.filter_by_instance(instance)
        return qs
def create_slug(instance,new_slag=None):
    slug = slugify(instance.item_name)
    if new_slag is not None:
        slug = new_slag
    qs = SellItemInfo.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slag = "%s-%s" %(slug,qs.first().id)
        return  create_slug(instance,new_slag=new_slag)
    return slug
def pre_save_item_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_item_receiver,sender=SellItemInfo)

class Comments(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(SellItemInfo)
    username = models.CharField(max_length=20,blank=False)
    content = models.TextField(max_length=200,blank=False)
    timestemp = models.DateTimeField(auto_now_add=True)

    # objects = CommentsManager()
    def __unicode__(self):
        return str(self.user.username)
