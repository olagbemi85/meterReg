from django.db import models
from django.urls import reverse

# Create your models here.


class Region(models.Model):  
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)  
    
    def __str__(self):
        return self.name
 
    
class AreaOffice(models.Model):
    region = models.ForeignKey(Region, related_name='area_office', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name