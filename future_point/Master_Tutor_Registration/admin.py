from django.contrib import admin

#Register your models here.
from . models import Notes_tbl
from . models import Works_tbl
from . models import minorwork_tbl 

admin.site.register(Notes_tbl)
admin.site.register(Works_tbl)
admin.site.register(minorwork_tbl)