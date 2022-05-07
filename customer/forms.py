from django import forms
from .models import Customer
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm



class CustomerUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['mobile_number','profile_pic']