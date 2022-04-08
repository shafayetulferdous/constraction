from django.db import models
from django.forms import ModelForm,TextInput,EmailInput

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True','True'),
        ('False','False'),

    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(blank=True,max_length=50)
    adress = models.CharField(blank=True,max_length=100)
    fax = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=50)
    facebook = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twtter = models.CharField(blank=True,max_length=50)
    aboutus = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    status = models.TextField(blank=True,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(blank=True,upload_to='images')
    

    def __str__(self):
        return self.title
    
   
   


class ContactMesssage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
        ('New','New'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200,blank=True)
    Note = models.CharField(max_length=200,blank=True)
    ip = models.CharField(max_length=200,blank=True)
    status = models.CharField(choices=STATUS,max_length=40,default='New')
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class ContactForm(ModelForm):
    class Meta:
        model = ContactMesssage
        fields = ['name','email','message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Sure name'}),
            'email': EmailInput(attrs={'class':'input','placeholder':'Write your email'}),
            'message': TextInput(attrs={'class':'input','placeholder':'write your message'}),
        }