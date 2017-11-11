from django.contrib import admin

# Register your models here.
from User.models import SellItemInfo,Chat

# Register your models here.

admin.site.register(SellItemInfo)
admin.site.register(Chat)
