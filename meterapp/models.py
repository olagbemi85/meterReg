from django.db import models
from account.models import User
from django.conf import settings
from django.urls import reverse
from django_countries.fields import CountryField
from uuid import uuid4








class MeterApplication(models.Model):
    application_number = models.CharField(max_length=255, null=True, unique=True)
    tracking_id =models.UUIDField(primary_key=True, default=uuid4, editable=False)
    state = models.CharField(max_length=255, null=True)
    premises_usage =  models.CharField(max_length=255, null=True)
    meter_type =  models.CharField(max_length=255, null=True)
    house_address = models.CharField(max_length=255, null=True)
    building_type = models.CharField(max_length=255, null=True)
    user_apply = models.CharField(max_length=255, null=True)
    electrical_personnel_name = models.CharField(max_length=255, null=True)
    account_number=  models.CharField(max_length=255, null=True)
    licence_number = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)
    sdate = models.DateField(max_length=255, null=True)
    electricalList = models.TextField(null=True)
    total_wattage = models.CharField(max_length=225, null=True)
    local_gov_area = models.CharField(max_length=225, null=True)
    area_office = models.CharField(max_length=225, null=True)
    regional_office = models.CharField(max_length=225, null=True)
    state = models.SlugField(max_length=225, null=False)

    def get_absolute_url(self):
        return reverse('meterapp:application_detail', args=[self.application_number])

    def __str__(self):
        return self.application_number
    

class ElectricalPersonnelCategory(models.Model):
    level_of_profession=models.CharField(max_length=25) 

    def __str__(self):
        return self.level_of_profession


class PremisesType(models.Model):
    premises_name = models.CharField(max_length=25)

    def __str__(self):
        return self.premises_name


class MeterType(models.Model):
    meter_name = models.CharField(max_length=25)

    def __str__(self):
        return self.meter_name


class PremisesUsage(models.Model):
    usage = models.CharField(max_length=25)

    def __str__(self):
        return self.usage
    

    