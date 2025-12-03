from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message":"You are authenticated!"})

# Create your views here.
def authView(request):
    if request.method == 'POST':
        #Populate the form with data from POST request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #save the new user of data is valid
            form.save()
            #redirect to login page
            return redirect("login")
    else:
        #if it is GET request, display blank form
        form = UserCreationForm()
    #pass the form (either blank or with error) to the template.
    return render(request, "registration/signup.html", {"form" : form})

def authView_login(request):
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form" : form} ) 