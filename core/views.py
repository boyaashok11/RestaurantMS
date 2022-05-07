from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')


def about(request):
    return render(request,'core/about.html')


def menu(request):
    return render(request,'core/menu.html')


def vacancies(request):
    return render(request,'core/career.html')

def table_booking(request):
    return render(request,'core/tablebooking.html')


def contact_us(request):
    pass


def sign_in(request):
    return render(request,'core/signin.html')