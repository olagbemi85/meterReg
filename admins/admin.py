from django.contrib import admin
from .models import *



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    


@admin.register(AreaOffice)
class AreOfficeAdmin(admin.ModelAdmin):
    list_display =['name']
