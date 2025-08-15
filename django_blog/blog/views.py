from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # because render will not change the url bar, even after you enter login credentials it will return you to register url(again)
        else:
            return render(request,'blog/register.html',{'form':form})
    else:
        form = UserRegisterForm()
    return render(request,'blog/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            return render(request,"blog/base.html")
        else:
            return render(request,'blog/login.html',{'form':form})
        
    else:
        form = AuthenticationForm()
    return render(request,'blog/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'blog/logout.html')
    
@login_required
def profile(request):
    return render(request,'blog/profile.html')

def base_view(request):
    return render(request,'blog/base.html')