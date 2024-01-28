
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'meterapp'


urlpatterns = [
	path('', views.index, name='home'),
	path('application/old/', views.meterApplication, name='application'),
	path('application/new/', views.meterApplicationNew, name='new_application'),	
]
