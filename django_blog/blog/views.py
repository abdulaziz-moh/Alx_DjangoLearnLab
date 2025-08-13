from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from . forms import SignupForm
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() # we may want it for automatic login
            
            return redirect('login')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
        else:
            return render(request,'login.html',{'form':form})
        
    else:
        form = AuthenticationForm()
    return render(request,'login .html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'loggedoutuser.html')
    
@login_required
def manageprofile_view(request):
    return redirect('profile')