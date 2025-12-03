from django.urls import path, include
from .views import authView, authView_login
from accounts.views import TestView 

urlpatterns = [
    path("signup/", authView, name = "signup"),
    path("login/", authView_login, name = "login"),
    # path("", include("django.contrib.auth.urls")), 
    path('test/', TestView.as_view(), name='test'),
] 