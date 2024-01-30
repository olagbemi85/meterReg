
from django.urls import path
from . import views
from .views import AModelUpdateView
from django.contrib.auth import views as auth_views


app_name = 'meterapp'


urlpatterns = [
	path('', views.index, name='home'),
	path('application/old/', views.meterApplication, name='application'),
	path('application/new/', views.meterApplicationNew, name='new_application'),
    path('detail/<slug:slug>/', views.application_detail, name='application_detail'),	
    path('edit-form/<slug:slug>/', views.editApplication, name='edit_form'),	
    #path('edit-form/<slug:slug>/', AModelUpdateView.as_view(), name='edit_form'),	
]
