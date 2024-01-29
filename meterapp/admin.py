from django.contrib import admin

from .models import *





@admin.register(MeterApplication)
class MeterApplicationAdmin(admin.ModelAdmin):
    list_display = ['building_type']


@admin.register(ElectricalPersonnelCategory)
class ElectricalPersonnelCategoryAdmin(admin.ModelAdmin):
    list_display = ['level_of_profession']


@admin.register(PremisesType)
class PremisesTypeAdmin(admin.ModelAdmin):
    list_display =['premises_name']


@admin.register(PremisesUsage)
class PremisesUsageAdmin(admin.ModelAdmin):
    list_display =['usage']


@admin.register(MeterType)
class MeterTypeAdmin(admin.ModelAdmin):
    list_display =['meter_name']