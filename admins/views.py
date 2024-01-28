

from django.shortcuts import render, redirect, get_object_or_404
#from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from .models import *
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
#from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
import datetime
from django.urls import reverse
import json
from django.http import JsonResponse
from django.contrib import messages





@login_required
def staff_area(request):


    return render(request, 'admins/staff.html')