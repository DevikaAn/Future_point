from django.contrib import admin

# Register your models here.
from .models import  notification_tbl,admin_tbl,course
admin.site.register(notification_tbl)
# admin.site.register(admin_tbl)
admin.site.register(course)