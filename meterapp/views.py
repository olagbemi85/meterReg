
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
import random





@login_required
def index(request):
    if request.user.is_authenticated:
        user = request.user
        profile = User.objects.get(email=user)
        pp= get_object_or_404(User, email=user) 
        
        #if request.user.is_superuser or request.user.is_staff:
            #return redirect('meterapp:home')
        if request.user.is_staff:
             form = MeterApplication.objects.filter(user_apply=user)
             return render(request, 'home.html',{'form':form})
            
        else:
            form = MeterApplication.objects.filter(user_apply=user)
            context={'form':form}
            return render(request, 'home.html',context)  
            
    else:
        return redirect('account:userlogin') 


@login_required
def meterApplication(request):
    return render(request, 'meterapp/meterapp.html')


@login_required
def meterApplicationNew(request):
    u = request.user
    users = User.objects.get(email=u)
    initial_data = {'user_apply': users.email }
    form = MeterApplicationForm(initial = initial_data) 
    context={'form':form}
    if request.method == 'POST':
          forms = MeterApplicationForm(request.POST )
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
          electricalList = request.POST['electricalList']
          total_wattage = request.POST['total_wattage']
          regional_office = request.POST['regional_office']
          area_office = request.POST['area_office']
          local_gov_area = request.POST['local_gov_area']
          user_apply = request.POST['user_apply']
          
          
          err = {'form' :forms}

          context={'state':state, 'premises_usage':premises_usage, 'meter_type':meter_type, 'house_address':house_address,
                   'building_type':building_type,'account_number':account_number,'electrical_personnel_name':electrical_personnel_name,'licence_number':licence_number,
                   'category':category,
                   'sdate':sdate,'electricalList':electricalList,'total_wattage':total_wattage, 'regional_office':regional_office, 'area_office':area_office, 'local_gov_area':local_gov_area, 'user_apply': user_apply}
          
          if forms.is_valid():
              '''
              foms = MeterApplication.objects.create(state=state, premises_usage=premises_usage, meter_type=meter_type, house_address=house_address,
                   building_type=building_type, account_number=account_number, electrical_personnel_name=electrical_personnel_name, licence_number=licence_number,
                   category=category,
                   sdate=sdate, electricalList=electricalList, total_wattage=total_wattage, regional_office=regional_office,
                     area_office=area_office, local_gov_area=local_gov_area, user=getUser.id)
              ''' 
              ap = random.randrange(0000,9999)
              ph = users.phone_number
              ap_no = 'AEDC'+'-'+str(ph)+'-'+str(ap)
              ap_number = ap_no
              
              foms = MeterApplication.objects.create(state=state, premises_usage=premises_usage, meter_type=meter_type, house_address=house_address,
                   building_type=building_type, account_number=account_number, electrical_personnel_name=electrical_personnel_name, licence_number=licence_number,
                   category=category,
                   sdate=sdate, electricalList=electricalList, total_wattage=total_wattage, regional_office=regional_office,
                     area_office=area_office, local_gov_area=local_gov_area, user_apply=user_apply, application_number=ap_number)         
              foms.save()
              print(foms)
              messages.success(request, 'Form successfully submitted')
              return redirect('meterapp:home')
          else:
              messages.error(request, 'form not submitted')
              explanation = form.errors.as_data()
              return render(request, 'meterapp/newMeterapp.html',err)
    #else:
         #form = MeterApplication()                  
    return render(request, 'meterapp/newMeterapp.html',{'form':form})


class UsernamevalidationView(View):
	def post(self, request):
		data =json.loads(request.body)
		username = data['username']
		if not str(username).isalnum():
			return JsonResponse({'username_error' : 'username should only contain character'}, status=400)
		if User.objects.filter(username=username).exists():
			return JsonResponse({'username_error' : 'sorry username in use'}, status=409)
		return JsonResponse({'username is valide' : True})
     

def application_detail(request, slug):
    datas = get_object_or_404(MeterApplication, application_number=slug)
    data = MeterApplication.objects.filter(application_number = slug).values('account_number', 'application_number', 'area_office', 'building_type', 'category', 'electricalList', 'electrical_personnel_name',
                                                                          'house_address', 'licence_number', 'local_gov_area', 'meter_type', 'premises_usage', 'regional_office', 'sdate', 'state', 'total_wattage', 'tracking_id', 'user_apply')
    station = slug
    return render(request, 'meterapp/application_data.html', {'data': data, 'st':station})   

@login_required
def editApplication(request, slug):
    user = request.user
    post = MeterApplication.objects.get(application_number=slug) 
    if request.method == 'POST':
         pass
         
    #context = {'post' : post}
    return render(request, 'merterapp/app_form_edit.html', context)	


@login_required
def profile_customer(request):
    user = request.user
    pp = User.objects.get(email=user)
    if request.method == 'POST':
        user_form = MeterApplication(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('authentication:edit-profile')
        else:
            messages.error(request, 'fail to save profile')
    else:
       	#try:
            user_form = MeterApplication(instance=request.user)
        #except:
            #profile = User.objects.create(user=request.user)
            #user_form = MeterApplication(instance=profile)
    return render(request, 'authentications/forms/update_profile.html', {'user_form': user_form, 'pp':pp })  
