from django.conf.urls import url
from User import views


app_name = 'User'

urlpatterns=[
        url(r'^home/$',views.userhome,name='home'),

        url(r'^profile/$',views.userprofile,name='profile'),
        url(r'^sellitem/$',views.sellitem,name='sellitem'),
]
