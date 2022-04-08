from django.shortcuts import render,get_object_or_404,redirect
from .models import Setting,ContactMesssage,ContactForm
from projectapp.models import Construction,ConstractionProjects
from service.models import Services
# Create your views here.
def home(request):
    setting = get_object_or_404(Setting,id=2)
    sliding_images = ConstractionProjects.objects.all()
    services = Services.objects.all().order_by('-id')[:4]
    context = {'setting':setting,'sliding_images':sliding_images,'services':services}
    return render(request,'homebase.html',context)


def AllProjects(request):
    setting = get_object_or_404(Setting,id=2)
    projects = ConstractionProjects.objects.all()
    context = {'setting':setting,'projects':projects}
    return render(request,'projects.html',context)



def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMesssage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            return redirect('contact')
    form = ContactForm
    context = {
        'form':form,
    }
    return render(request,'contact.html',context)


           

 
def singleproject(request,id):
    setting = get_object_or_404(Setting,id=2)
    singlepro = get_object_or_404(ConstractionProjects,id=id)
    context = {'setting':setting,'singleproject':singlepro}
    return render(request,'singleproject.html',context)

def Aboutus(request):
    setting = get_object_or_404(Setting,id=2)
    context = {'setting':setting}
    return render(request,'about.html',context)
