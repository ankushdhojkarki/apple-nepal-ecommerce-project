from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def authView(request):
    form = UserCreationForm
    return render(request, "accounts/signup.html", {"form" : form})

def authView_login(request):
    form = AuthenticationForm
    return render(request, "accounts/login.html", {"form" : form} )