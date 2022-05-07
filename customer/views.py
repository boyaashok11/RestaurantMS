from django.shortcuts import render
from .forms import CustomerUserForm,CustomerForm


# Create your views here.
def customer_sign_up(request):
    user_form=CustomerUserForm()
    customer_form=CustomerForm()
    return render(request,'customer/signup.html',{'userform':user_form,'customerform':customer_form})