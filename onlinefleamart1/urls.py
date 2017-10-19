from django.conf.urls import url
from django.contrib import admin
from firstapp import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler500
# handler403 = 'firstapp.views.permission_denied'
# handler404 = 'firstapp.views.page_not_found'
# handler500 = 'firstapp.views.server_error'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^fleamart/',include('firstapp.urls')),
    # url(r'^$',include('firstapp.urls')),
    url(r'^home/$',views.userhome,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',views.userlogout,name='logout'),

    url(r'^profile/$',views.userprofile,name='profile'),

    # url(r'^login/', views.login,name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'firstapp.views.error_404'
handler500 = 'firstapp.views.error_500'
