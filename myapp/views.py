from django.shortcuts import render , redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
import random
import http.client
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .mixin import MessageHandler
from .forms import DLForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        mobile_no = request.POST.get('mobile_no')
        profile = Profile.objects.get(mobile_no=mobile_no)
        # if not profile.exists():
        #     return redirect ('/register/')

        profile.otp = random.randint(1000,9999)
        profile.save()
        message_handler = MessageHandler(mobile_no, profile.otp).send_otp_on_mobile()
        return redirect(f'/otp/{profile.uid}')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        user = User.objects.create(username=username)
        profile = Profile.objects.create(user=user, mobile_no=mobile_no)
        return redirect('/')

    return render(request,'register.html')

def otp(request,uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile =Profile.objects.get(uid=uid)

        if otp == profile.otp:
            login(request, profile.user)
            return redirect('/dashboard/')

        return redirect(f'otp{uid}')

    return render(request,'otp.html')

def dashboard(request):
    return render(request,'dashboard.html')


#logout view
def user_logout(request):
    logout(request)
    messages.success(request,'Logout successfully !!')
    return HttpResponseRedirect('/register/')


def driving_licence(request):
    if request.method == "POST":
        form = DLForm(request.POST)
        
        if form.is_valid():
            form.save()

    else:
        form = DLForm()
    return render(request,'dlform.html',{'form':form})

