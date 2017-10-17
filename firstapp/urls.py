from django.conf.urls import url
from firstapp import views


app_name = 'firstapp'

urlpatterns=[

    url(r'^$',views.login,name='login'),

]
