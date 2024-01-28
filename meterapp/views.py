
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from .models import *
from .forms import MeterApplicationForm
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from django.views import View
import datetime
from django.urls import reverse
import json
from django.http import JsonResponse
from django.contrib import messages





@login_required
def index(request):
    if request.user.is_authenticated:
        user = request.user
        profile = User.objects.get(email=user)
        pp= get_object_or_404(User, email=user) 
        
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admins:home')
            
        else:
            form = MeterApplication.objects.filter(user=user)
            context={'form':form}
            return render(request, 'home.html',context)  
            
    else:
        return redirect('authentication:userlogin') 


@login_required
def meterApplication(request):
    return render(request, 'meterapp/meterapp.html')

'''
@login_required
def meterApplicationNew(request):
    form = MeterApplicationForm()
    context={'form':form}
    if request.method == 'POST':
          user_form = MeterApplicationForm(request.POST)
          state = request.POST['state']
          premises_usage = request.POST['premises_usage']
          meter_type = request.POST['meter_type']
          house_address = request.POST['house_address']
          building_type = request.POST['building_type']
          account_number = request.POST['account_number']
          electrical_personnel_name = request.POST['electrical_personnel_name']
          licence_number = request.POST['licence_number']
          category = request.POST['category']
          sdate = request.POST['sdate']
          electrical_point_list = request.POST['electrical_point_list']
          total_wattage = request.POST['total_wattage']
          regional_office = request.POST['regional_office']
          area_office = request.POST['area_office']
          local_gov_area = request.POST['local_gov_area']

          context={'state':state, 'premises_usage':premises_usage, 'meter_type':meter_type, 'house_address':house_address,
                   'building_type':building_type,'account_number':account_number,'electrical_personnel_name':electrical_personnel_name,'licence_number':licence_number,
                   'category':category,
                   'sdate':sdate,'electrical_point_list':electrical_point_list,'total_wattage':total_wattage, 'regional_office':regional_office, 'area_office':area_office, 'local_gov_area':local_gov_area,}
          if user_form.is_valid():
              
              form = MeterApplication.objects.create(state=state, premises_usage=premises_usage, meter_type=meter_type, house_address=house_address,
                   building_type=building_type, account_number=account_number, electrical_personnel_name=electrical_personnel_name, licence_number=licence_number,
                   category=category,
                   sdate=sdate, electrical_point_list=electrical_point_list, total_wattage=total_wattage, regional_office=regional_office, area_office=area_office, local_gov_area=local_gov_area)
                   
              form.save()
              messages.success(request, 'Form successfully submitted')
              redirect('meterapp:home')
          else:
              messages.error(request, 'form not submitted')
              return render(request, 'meterapp/newMeterapp.html')            
    return render(request, 'meterapp/newMeterapp.html',{'form':form})


@login_required
def input_user(request):
    u = request.user
    users = User.objects.get(email=u)
    return {'users':users}

'''    

@login_required
def meterApplicationNew(request):
    u = request.user
    users = User.objects.get(email=u)
    form = MeterApplicationForm()
    context={'form':form}
    if request.method == 'POST':
          application_form = MeterApplicationForm(request.POST, instance=request.user)
          state = request.POST['state']
          premises_usage = request.POST['premises_usage']
          meter_type = request.POST['meter_type']
          house_address = request.POST['house_address']
          building_type = request.POST['building_type']
          account_number = request.POST['account_number']
          electrical_personnel_name = request.POST['electrical_personnel_name']
          licence_number = request.POST['licence_number']
          category = request.POST['category']
          sdate = request.POST['sdate']
          electrical_point_list = request.POST['electrical_point_list']
          total_wattage = request.POST['total_wattage']
          regional_office = request.POST['regional_office']
          area_office = request.POST['area_office']
          local_gov_area = request.POST['local_gov_area']
          user = request.POST['user']
          
          
          err = {'form' :application_form}

          context={'state':state, 'premises_usage':premises_usage, 'meter_type':meter_type, 'house_address':house_address,
                   'building_type':building_type,'account_number':account_number,'electrical_personnel_name':electrical_personnel_name,'licence_number':licence_number,
                   'category':category,
                   'sdate':sdate,'electrical_point_list':electrical_point_list,'total_wattage':total_wattage, 'regional_office':regional_office, 'area_office':area_office, 'local_gov_area':local_gov_area, 'user':user}
          print(context)
          if application_form.is_valid(): 
              forms = MeterApplication.objects.create(state=state, premises_usage=premises_usage, meter_type=meter_type, house_address=house_address,
                   building_type=building_type, account_number=account_number, electrical_personnel_name=electrical_personnel_name, licence_number=licence_number,
                   category=category,
                   sdate=sdate, electrical_point_list=electrical_point_list, total_wattage=total_wattage, regional_office=regional_office, area_office=area_office, local_gov_area=local_gov_area, user=user)    
              forms.save()
              print(forms)
              messages.success(request, 'Form successfully submitted')
              return redirect('meterapp:home')
          else:
              messages.error(request, 'form not submitted')
              explanation = form.errors.as_data()
              return render(request, 'meterapp/newMeterapp.html',err)            
    return render(request, 'meterapp/newMeterapp.html',{'form':form, 'users':users})


class UsernamevalidationView(View):
	def post(self, request):
		data =json.loads(request.body)
		username = data['username']
		if not str(username).isalnum():
			return JsonResponse({'username_error' : 'username should only contain character'}, status=400)
		if User.objects.filter(username=username).exists():
			return JsonResponse({'username_error' : 'sorry username in use'}, status=409)
		return JsonResponse({'username is valide' : True})
