from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "authentication"

urlpatterns = [

    path('register/',views.SignUpView.as_view(), name="register"),
    path('login/',views.login_view, name="login"),

    #path('logout/',views.logout_view, name="logout"),
   
    
]