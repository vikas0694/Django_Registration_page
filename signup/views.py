from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username = username, email = None, password = password)
            messages.success(request,'Registration Successfull')
            return HttpResponseRedirect('/signup/')
    else:
        form1 = userform()
    return render(request,'signup.html',{'form':form1})
def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        #emailid = request.POST['email']
        password = request.POST['pass']
        try:
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return render(request,'welcome.html')
            else:
                messages.error(request,'Ivalid username or password!')
        except ObjectDoesNotExist:
            print("Invalid user")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
