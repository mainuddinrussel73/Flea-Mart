from django.contrib import admin

# Register your models here.
from User.models import SellItemInfo,Chat,Notification,Comments

# Register your models here.

admin.site.register(SellItemInfo)
admin.site.register(Chat)
admin.site.register(Notification)
admin.site.register(Comments)
