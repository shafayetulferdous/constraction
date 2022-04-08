from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/s',views.Contact,name='contact'),
    path('projects/',views.AllProjects,name='projects'),
    path('projects/<int:id>/',views.singleproject,name='singleproject'),
    path('about/',views.Aboutus,name='aboutus'),
]