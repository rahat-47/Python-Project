from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Favorite


from django.shortcuts import render


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def contact(request):
    return render(request, 'contact.html')
def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html')
    else:
        messages.warning(request, 'Please login first to access this page.')
        return render(request, 'login.html')  # Assuming you have a login page named 'login.html'



@login_required
def about(request):
    return render(request, 'about.html')
def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        messages.warning(request, 'Please login first to access this page.')
        return render(request, 'login.html')  # Assuming you have a login page named 'login.html'

@login_required
def news(request):
    return render(request, 'news.html')
def news(request):
    if request.user.is_authenticated:
        return render(request, 'news.html')
    else:
        messages.warning(request, 'Please login first to access this page.')
        return render(request, 'login.html')  # Assuming you have a login page named 'login.html'
    
    

@login_required
def destinations(request):
    return render(request, 'destinations.html')
# def reset_password(request):
#     return render(request, 'password.html')
def destinations(request):
    if request.user.is_authenticated:
        return render(request, 'destinations.html')
    else:
        messages.warning(request, 'Please login first to access this page.')
        return render(request, 'login.html')  # Assuming you have a login page named 'login.html'


@login_required
def home(request):
    return render(request, 'home.html')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        messages.warning(request, 'Please login first to access this page.')
        return render(request, 'login.html')  # Assuming you have a login page named 'login.html'








def dhaka(request):
    return render(request, 'dhaka.html')

def chittagong(request):
    return render(request, 'chittagong.html')

def barishal(request):
    return render(request, 'barishal.html')

def coxs_bazar(request):
    return render(request, 'coxs_bazar.html')


def bandarban(request):
    return render(request, 'bandarban.html')

def bogura(request):
    return render(request, 'bogura.html')

def jessore(request):
    return render(request, 'jessore.html')

def khulna(request):
    return render(request, 'khulna.html')

def rajshahi(request):
    return render(request, 'rajshahi.html')


def mouluvibazar(request):
    return render(request, 'mouluvibazar.html')

def rangamati(request):
    return render(request, 'rangamati.html')

def rangpur(request):
    return render(request, 'rangpur.html')

def sylhet(request):
    return render(request, 'sylhet.html')


def template(request):
    # Add logic to retrieve user profile data if needed
    return render(request, 'template.html')


#-----------------------------------------------------------------






  #load csv file
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import context,loader
import csv


#-------------------dhaka-------------
def dhaka_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/dhaka_hotel.csv"
    with open(file_path, mode='r') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))




def dhaka_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_dhaka.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))



#----------------chittagong--------------------------------------

def chittagong_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/chittagong_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))



def chittagong_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/04_dhaka_to_chittagong.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))


def chittagong_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_chittagong.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))



#-------------coxsbazar---------------------------------



def cosx_bazar_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/cox_bazar_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def cosx_bazar_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/05_dhaka_to_cox_bazar.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def cosx_bazar_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_cox_bazar.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))



#-----------------barishal-------------------------

def barishal_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/barisal_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def barishal_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/01_dhaka_to_barisal.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def barishal_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_barisal.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))



#---------------------bandarban------------------------

def bandarban_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/Bandarban_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def bandarban_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/02_dhaka_to_bandarban.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def bandarban_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_bandarban.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))


#---------------------bogura------------------------

def bogura_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/bogra_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def bogura_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/03_dhaka_to_bogura.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def bogura_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_bogura.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))


#---------------------jessore------------------------

def jessore_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/jessore_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def jessore_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/06_dhaka_to_jessore.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def jessore_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_jessore.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))


#---------------------khulna------------------------

def khulna_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/Khulna_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def khulna_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/07_dhaka_to_khulna.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def khulna_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_khulna.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))


#--------------rajshahi-------------------------

def rajshahi_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/rajshahi_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rajshahi_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/09_dhaka_to_rajshahi.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rajshahi_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_rajshahi.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

#-------------------mouluvibazar--------------------------------

def mouluvibazar_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/Maulvibazar_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def mouluvibazar_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/08_dhaka_to_moulvibazar.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def mouluvibazar_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_moulvibazar.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

#-----------------------rangamati-----------------------------
def rangamati_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/Rangamati_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rangamati_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/10_dhaka_to_rangamati.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rangamati_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_rangamati.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

#-----------------------rangpur-------------------------------------

def rangpur_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/rangpur_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rangpur_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/11_dhaka_to_rangpur.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def rangpur_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_rangpur.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

# ---------------------sylhet---------------------------

def sylhet_hotel(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/sylhet_hotel.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Hotel_name','Hotel_currency','Hotel_price','Hotel_properties']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def sylhet_bus(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/12_dhaka_to_sylhet.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Bus_name','Departure_time','Arrival_time','Price/seat']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))

def sylhet_restaurant(request):
    template = loader.get_template('template.html')
    context = {'name':'xyz'}
    # file = open("static/dhaka_hotel.csv")
    file_path = "static/restaurant_sylhet.csv"
    with open(file_path, mode='r',encoding='utf-8') as file:
     csvreader = csv.reader(file)
     headers = next(csvreader)
     rows = [row for row in csvreader]
    #  context['headers'] = headers 
    context = {'headers':['Restaurant Name','Rating','Address']} 
    context['rows'] = rows
    return HttpResponse(template.render(context,request))





#--------------------------------------------------------------------





def user_dashboard(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'favorites': favorites})


# @login_required
# @require_POST
# def add_favorite(request):
#     row_data = request.POST.get('row_data')
#     Favorite.objects.create(user=request.user, row_data=row_data)
#     return redirect('user_dashboard')

def add_favorite(request):
    if request.method == 'POST':
        row_data = request.POST['row_data']
        user = request.user

        # Check if this row data is already in the user's favorites
        if Favorite.objects.filter(user=user, row_data=row_data).exists():
            messages.info(request, 'This item is already in your favorites.')
        else:
            # Add to favorites
            favorite = Favorite(user=user, row_data=row_data)
            favorite.save()
            messages.success(request, 'Added to your favorites!')

        return redirect('user_dashboard')  # Redirect to an appropriate page

@login_required
@require_POST
def remove_favorite(request):
    row_data = request.POST.get('row_data')
    Favorite.objects.filter(user=request.user, row_data=row_data).delete()
    return redirect('user_dashboard')
    
    








