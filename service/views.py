from django.shortcuts import render,get_object_or_404,redirect
from .models import Services,ourTeam
from comapp .models import Setting
# Create your views here.

def ServicesView(request):
    service = Services.objects.all()
    setting = get_object_or_404(Setting,id=2)
    context = {
        'service':service,
        'setting':setting
    }
    return render(request,'service.html',context)



def TeamView(request):
    team = ourTeam.objects.all()
    setting = get_object_or_404(Setting,id=2)
    context = {
        'team':team,
        'setting':setting
    }
    return render(request,'team.html',context)