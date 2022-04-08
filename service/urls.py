from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.ServicesView,name='services'),
    path('team/',views.TeamView,name='team'),
]
  

