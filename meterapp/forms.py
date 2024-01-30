from  django import forms
from django.forms.widgets import NumberInput
from .models import *
from admins.models import AreaOffice, Region
from .views import *
from account.models import State, LGA,User
#from .views import input_user
 

class MeterApplicationForm(forms.ModelForm):
    account_number =forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Meter Number', 'type':'text'}))
    #state =forms.ModelChoiceField(required=True, queryset=State.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #area_office = forms.ModelChoiceField(required=True, queryset= AreaOffice.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #regional_office = forms.ModelChoiceField(required=True, queryset=Region.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #premises_usage = forms.ModelChoiceField(required=True, queryset=PremisesUsage.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #meter_type = forms.ModelChoiceField(required=True, queryset=MeterType.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #user_apply = forms.ModelChoiceField(required=True, queryset=User.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    user_apply = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'applicant/owners email', 'type':'text'}))
    house_address = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Premises Adrress', 'type':'text'}))
    #building_type = forms.ModelChoiceField(required=True, queryset=PremisesType.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    electrical_personnel_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Athurized Personnel in charge of the premises', 'type':'text'}))
    licence_number = forms.IntegerField( widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'License Number'}))
    sdate = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class':'form-control', "onchange":"checkStartDate()", "id":"sdate"}))
    electricalList = forms.CharField(max_length=200,  widget=forms.Textarea(attrs ={'class':'form-control' ,'placeholder':'applances list', 'type':'text'}))
    total_wattage = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Total Wattage', 'type':'text'}))
    #category = forms.ModelChoiceField(required=True, queryset=ElectricalPersonnelCategory.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    #local_gov_area = forms.ModelChoiceField(required=True, queryset=LGA.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))

    
    def __init__(self, *args, **kwargs):
        super(MeterApplicationForm, self).__init__(*args, **kwargs)
        self.fields['building_type'].widget = forms.Select(choices = PremisesType.objects.values_list('premises_name','premises_name'))
        self.fields['state'].widget = forms.Select(choices = State.objects.values_list('stateName','stateName'), attrs={'class': 'form-control'})
        self.fields['area_office'].widget = forms.Select(choices = AreaOffice.objects.values_list('name','name'), attrs={'class': 'form-control'})
        self.fields['regional_office'].widget = forms.Select(choices = Region.objects.values_list('name','name'), attrs={'class': 'form-control'})
        self.fields['premises_usage'].widget = forms.Select(choices = PremisesUsage.objects.values_list('usage','usage'), attrs={'class': 'form-control'})
        self.fields['meter_type'].widget = forms.Select(choices = MeterType.objects.values_list('meter_name','meter_name'), attrs={'class': 'form-control'})
        self.fields['local_gov_area'].widget = forms.Select(choices =LGA.objects.values_list('localGovName','localGovName'), attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(choices =ElectricalPersonnelCategory.objects.values_list('level_of_profession','level_of_profession'), attrs={'class': 'form-control'})

    class Meta():
        model = MeterApplication
        fields=('account_number','state','area_office','regional_office','premises_usage','meter_type','house_address', 'user_apply',
                'building_type','electrical_personnel_name','licence_number','sdate','electricalList','total_wattage','category','local_gov_area')
        

class MeterApplicationFormupdate(forms.ModelForm):
    account_number =forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Meter Number', 'type':'text'}))
    user_apply = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'applicant/owners email', 'type':'text'}))
    house_address = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Premises Adrress', 'type':'text'}))
    electrical_personnel_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Athurized Personnel in charge of the premises', 'type':'text'}))
    licence_number = forms.IntegerField( widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'License Number'}))
    sdate = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class':'form-control', "onchange":"checkStartDate()", "id":"sdate"}))
    electricalList = forms.CharField(max_length=200,  widget=forms.Textarea(attrs ={'class':'form-control' ,'placeholder':'applances list', 'type':'text'}))
    total_wattage = forms.CharField(max_length=100,  widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Total Wattage', 'type':'text'}))

    def __init__(self, *args, **kwargs):
        super(MeterApplicationForm, self).__init__(*args, **kwargs)
        self.fields['building_type'].widget = forms.Select(choices = PremisesType.objects.values_list('premises_name','premises_name'))
        self.fields['state'].widget = forms.Select(choices = State.objects.values_list('stateName','stateName'), attrs={'class': 'form-control'})
        self.fields['area_office'].widget = forms.Select(choices = AreaOffice.objects.values_list('name','name'), attrs={'class': 'form-control'})
        self.fields['regional_office'].widget = forms.Select(choices = Region.objects.values_list('name','name'), attrs={'class': 'form-control'})
        self.fields['premises_usage'].widget = forms.Select(choices = PremisesUsage.objects.values_list('usage','usage'), attrs={'class': 'form-control'})
        self.fields['meter_type'].widget = forms.Select(choices = MeterType.objects.values_list('meter_name','meter_name'), attrs={'class': 'form-control'})
        self.fields['local_gov_area'].widget = forms.Select(choices =LGA.objects.values_list('localGovName','localGovName'), attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(choices =ElectricalPersonnelCategory.objects.values_list('level_of_profession','level_of_profession'), attrs={'class': 'form-control'})

    class Meta():
        model = MeterApplication
        fields=('account_number','state','area_office','regional_office','premises_usage','meter_type','house_address', 'user_apply',
                'building_type','electrical_personnel_name','licence_number','sdate','electricalList','total_wattage','category','local_gov_area')
        




