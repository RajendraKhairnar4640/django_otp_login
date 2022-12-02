from django.shortcuts import render
from django.contrib.auth.models import AbstractUser

# Create your views here.

def signup(request):
    fm = AbstractUser()
    return render(request, "accounts/signup.html",{"form":fm})