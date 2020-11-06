from django.contrib import admin
from django.urls import path , include
from aestesting.views import User_Signup,SerData

urlpatterns = [
  
    path('User_Signup',User_Signup.as_view()),
    path('SerData',SerData.as_view()),
]