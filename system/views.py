from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction
from .models import *
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def my_vehicles(request):
    try:
        client = Client.objects.get(user=request.user)
    except Client.DoesNotExist:
        return JsonResponse([], safe=False)

    vehicles = Vehicle.objects.filter(owner=client)

    data = [
        {
            "plate": v.plate,
            "color": v.color,
            "type": v.type,
            "VIN": v.VIN,
            "latitude": v.latitude,
            "longitude": v.longitude
        }
        for v in vehicles
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
def upload_vehicle_data(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        body = json.loads(request.body.decode('utf-8'))
        vehicle_id = body.get("vehicle_id")
        lat = body.get("latitude")
        lng = body.get("longitude")

        # find vehicle by plate number OR VIN (you choose)
        vehicle = Vehicle.objects.get(plate=vehicle_id)

        vehicle.latitude = lat
        vehicle.longitude = lng
        vehicle.save()

        return JsonResponse({'status': 'success', 'updated': vehicle_id})

    except Vehicle.DoesNotExist:
        return JsonResponse({'error': 'Vehicle not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def RegisterUser(request):
    if request.method =='POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            request.session['temp_user'] = form.cleaned_data['username']
            request.session['temp_email'] = form.cleaned_data['email']
            request.session['temp_password'] = form.cleaned_data['password1']
            return redirect('system:register2')
        messages.error(request,'Correct errors below')
    form = UserRegistration()
    return render(request,'signup.html',{'form':form})


@transaction.atomic
def Register2(request):
    required = ['temp_user', 'temp_email', 'temp_password']
    for key in required:
        if key not in request.session:
            return redirect('system:signup')

    if request.method == 'POST':
        form = CompleteProfile(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.session['temp_user'],
                email=request.session['temp_email'],
                password=request.session['temp_password']
            )

            # ✅ SAFE CLIENT CREATION
            client, created = Client.objects.get_or_create(user=user)

            vehicle = form.save(commit=False)
            vehicle.owner = client
            vehicle.save()

            for key in required:
                request.session.pop(key, None)
            login(request, user)
            return redirect('system:finish')

    form = CompleteProfile()
    return render(request, 'register2.html', {'form': form})

def cancel_reg(request):
    required = ['temp_user', 'temp_email', 'temp_password']
    for key in required:
        request.session.pop(key,None)
        return redirect('system:signup')

def finish_page(request):
    return render(request,'finish.html')

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('system:dashboard')
        return redirect('system:landing')

    if request.method =='POST':
        form = UserLogging(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if user.is_superuser or user.is_staff:
                    return redirect('system:dashboard')
                return redirect('system:landing')
            else:
                messages.error(request,'Invalid  User not Found')
                return render(request,'login.html')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('system:login')

    else:
        form = UserLogging()
        return render(request,'login.html',{'form': form})


def landing_page(request):
    return render(request,'landing.html')

@login_required
def dashboard(request):
    client = Client.objects.all()
    user_count = User.objects.count()
    vehicles = Vehicle.objects.select_related('owner__user')
    total_cars = Vehicle.objects.count()
    return render(request,'dashboard.html',{'user_count':user_count,'vehicles':vehicles,'total_cars':total_cars})

@login_required
def vehicle_details(request, vehicle_id):
    info = get_list_or_404(Vehicle,id=vehicle_id)
    return render(request,'users.html',{'info':info})

@login_required
def layer(request):
    return render(request,'layer.html',{})
@login_required
def home(request):
    return render(request,'home.html',{})

@login_required
def map(request):
    return render(request,'map.html',{})

def transanction(request):
    return render(request,'transanction.html',{})

@login_required
def Analysis(request):
    return render(request,'analysis.html',{})

@login_required
def info(request):
    user = request.user
    profile = request.user.client

    client = Client.objects.get(user=user)
    vehicle = Vehicle.objects.filter(owner=client)

    if request.method =='POST':
        form = ProfileUpdate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated')
            redirect('system:home')
        else:
            messages.error(request,'Invalid form')
            redirect('system:home')
    form = ProfileUpdate()
    return render(request,'info.html',{'vehicle':vehicle,'profile':profile,'form':form})


def logoutUser(request):
    logout(request)
    user = request.user
    return redirect('system:login')
