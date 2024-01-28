from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'admins'


urlpatterns = [
    path('', staff_area, name='home'),
 

]
