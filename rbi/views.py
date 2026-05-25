from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

def loginview(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm(request)
    return render(request,'login.html',{'form':form})

@login_required
def home(request):
    return render(request,'base.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


