from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from . forms import SignupForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() # we may want it for automatic login

            return redirect('login') # because render will not change the url bar, even after you enter login credentials it will return you to register url(again)
        else:
            return render(request,'registration.html',{'form':form})
    else:
        form = SignupForm()
    return render(request,'registration.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            return render(request,"base.html")
        else:
            return render(request,'login.html',{'form':form})
        
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'logout.html')
    
# @login_required
def profile_view(request):
    return render(request,'profile.html')

def base_view(request):
    return render(request,'base.html')