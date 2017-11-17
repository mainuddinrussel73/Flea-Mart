from django.conf.urls import url
from User import views


app_name = 'User'

urlpatterns=[
        url(r'^home/$',views.userhome,name='home'),
        url(r'^(?P<slug>[\w-]+)details/$',views.showitem,name='details'),
        url(r'^profile/$',views.userprofile,name='profile'),
        url(r'^sellitem/$',views.sellitem,name='sellitem'),
        url(r'^post/$', views.Post, name='post'),
        url(r'^notification/$', views.Notifications, name='notification'),
        url(r'^notificationupdate/$', views.Notificationsupdate, name='notificationupdate'),
        url(r'^messages/$', views.Messages, name='messages'),

]
