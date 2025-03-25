from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request,'index.html')


def Login(request):
    if request.method == 'POST':
        user1 = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username = user1,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('dashAdmin')
            elif user.is_trainer:
                return redirect('dashTrainer')
            elif user.is_member:
                return redirect('dashMember')
            else:
                messages.info(request,'Invalid Credentials')
    return render(request,'login.html')


