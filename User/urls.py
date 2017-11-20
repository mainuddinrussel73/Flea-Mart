from django.conf.urls import url
from User import views
from django.contrib import admin
from .views import (
    PostLikeAPIToggle,

    )


app_name = 'User'

urlpatterns=[
        url(r'^home/$',views.userhome,name='home'),
        url(r'^(?P<slug>[\w-]+)likesupdate/$',views.Likesupdate,name='likesupdate'),
        url(r'^(?P<slug>[\w-]+)details/$',views.showitem,name='details'),
        # url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
        url(r'^api/(?P<slug>[\w-]+)/likes/$',PostLikeAPIToggle.as_view(),name='likes-api-toggle'),
        url(r'^profile/$',views.userprofile,name='profile'),
        url(r'^sellitem/$',views.sellitem,name='sellitem'),
        url(r'^post/$', views.Post, name='post'),
        url(r'^notification/$', views.Notifications, name='notification'),
        url(r'^messages/$', views.Messages, name='messages'),



]
