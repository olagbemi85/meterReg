from django.shortcuts import render
from .models import *
from django.views import View
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from validate_email import validate_email
from django.http import JsonResponse
import json

from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError #force_text
from django.utils.http import urlsafe_base64_encode
from .utils import token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

#import random
from .backends import EmailPhoneUsernameAuthenticationBackend as EoP


@login_required
def profile(request):
    user = request.user
    post = User.objects.get(email=user) # This query object give logged in user profile
    context = {'post' : post}
    return render(request, 'account/profile-detail.html', context)


@login_required
def profile_edit(request):
    user = request.user
    pp = User.objects.get(email=user)
    if request.method == 'POST':
        user_form = UserFormUpdate(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('account:edit-profile')
        else:
            messages.error(request, 'fail to save profile')
    else:
       	#try:
            user_form = UserFormUpdate(instance=request.user)
        #except:
            #profile = User.objects.create(user=request.user)
            #user_form = UserFormUpdate(instance=profile)
    return render(request, 'account/update_profile.html', {'user_form': user_form, 'pp':pp })


class Register(View):
	user_form = UserForm()
	def get(self, request, data=None):
		if request.user.is_authenticated:
			return redirect('meterapp:home')
		else:
			messages.success(request, 'Please fill in your data')
			context = {'form': self.user_form}
			return render(request, 'account/register.html', context) 
	
	def post(self, request):
		if request.method == 'POST':
			#user_form = UserForm(data=request.POST)
			user_form = UserForm(request.POST)
			username = request.POST['username']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']
			password = request.POST['password']
			nin_number = request.POST['nin_number']
			phone_number = request.POST['phone_number']
			err = {'form' :user_form}

			context = {
				'username':username, 'email':email, 'first_name':first_name, 'last_name':last_name,
				  'password':password, 'phone_number':phone_number, 'nin_number':nin_number 
				}

			#password1 = self.cleaned_data.get("password1")
			#password2 = self.cleaned_data.get("password2")
			#if password1 and password2 and password1 != password2:ayobami1234
				#raise ValidationError("Passwords don't match")
			#return password2    
			if user_form.is_valid():
				if not User.objects.filter(username = username).exists():
					if not User.objects.filter(email = email).exists():
						if len(password) < 8:
							messages.error(request, 'password too short')
							return render(request, 'account/register.html', err)
                        
						user = User.objects.create_user(username=username, email=email, first_name=first_name,
									   last_name=last_name, nin_number=nin_number, phone_number=phone_number)
						#create_user_profile()
						user.save()
						user.set_password(password)
						user.save()
						'''
						uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

						domain = get_current_site(request).domain
						link = reverse('activate', kwargs={'uidb64':uidb64, 'token': token_generator.make_token(user)})
						activate_url = 'http://'+domain+link
						email_subject = 'activate your account'
						email_body = 'thank you for register with us '+user.username + 'Please use the link to verify your account\n' +activate_url 
						email = EmailMessage(email_subject, email_body, 'noreply@semycolon.com',[email], )
						import urllib3
						proxy_support = urllib3.ProxyHandler({"http":"http://61.233.25.166:80"})
						opener = urllib3.build_opener(proxy_support)
						urllib3.install_opener(opener)

						email.send(fail_silently = False)
						'''

						messages.success(request, 'Account successfully created')
						return redirect('account:userlogin')                         
					messages.error(request, 'e-mail taken')
					return render(request, 'account/register.html', err)
				messages.error(request, 'user exist')
				return render(request, 'account/register.html', err)
			return render(request, 'account/register.html', err)
			#return self.get(request, msg)



class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('meterapp:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        messages.success(request, 'please input your email and password', 'success')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = EoP.authenticate(request, username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                #messages.success(request, 'You have successfully logged in!', 'success')
                return redirect('meterapp:home')
            else:
                messages.error(request, 'Your email or password is incorrect!', 'danger')
        return render(request, self.template_name, {'form': form})
    

class UsernamevalidationView(View):
	def post(self, request):
		data =json.loads(request.body)
		username = data['username']
		if not str(username).isalnum():
			return JsonResponse({'username_error' : 'username should only contain character'}, status=400)
		if User.objects.filter(username=username).exists():
			return JsonResponse({'username_error' : 'sorry username in use'}, status=409)
		return JsonResponse({'username is valide' : True})

class EmailvalidationView(View):
	# install mode called validate-email by using pip(pip install validate-email)
	def post(self, request):
		data =json.loads(request.body)
		email = data['email']
		if not validate_email(email):
			return JsonResponse({'email_error' : 'email is invalid'}, status=400)
		if User.objects.filter(email=email).exists():
			return JsonResponse({'email_error' : 'sorry email in use'}, status=409)
		return JsonResponse({'email is valide' : True})