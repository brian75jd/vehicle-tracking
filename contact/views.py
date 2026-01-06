from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SendUsMessage
from .models import SendMessage
from system.models import *
from django.contrib import messages

@login_required
def feedback(request):
    if request.method =='POST':
        form = SendUsMessage(request.POST)
        if form.is_valid():
            context = form.cleaned_data.get('content')
            SendMessage.objects.create(
                sender = request.user,
                content = context,
                email = request.user.email,
            )
            messages.success(request,'Messages was submitted successfully')
            return redirect("contact:feedback")
        messages.error(request,'something went wrong')
        return redirect('contact:feedback')
    form = SendUsMessage()
    return render(request,'about.html',{'form':form})


@login_required
def AdminMessages(request):
    message = SendMessage.objects.order_by('-date_Sent')
    return render(request,'messages.html',{'message':message})

@login_required
def message_details(request,message_id):
    messages = get_object_or_404(SendMessage,id=message_id)
    return render(request,'message_detail.html',{'message':messages})

@login_required
def Analysis(request):
    client = Client.objects.all()
    user_count = User.objects.count()
    vehicles = Vehicle.objects.select_related('owner__user')
    total_cars = Vehicle.objects.count()
    return render(request,'analysis.html',{'user_count':user_count,'vehicles':vehicles,'total_cars':total_cars})


@login_required
def Live_Tracking(request):
    return render(request,'liveTrack.html',{})
