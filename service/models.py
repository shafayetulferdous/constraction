from django.db import models
from projectapp.models import Construction
# Create your models here.
class Services(models.Model):
    StATUS = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=100)
    title_icon = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=StATUS)
    detaiil = models.TextField()

    def __str__(self):
        return self.title
    
class ourTeam(models.Model):

    StATUS = (
        ('True','True'),
        ('False','False'),
    )

    name = models.CharField(max_length=100)
    espicial_category = models.ForeignKey(Construction,on_delete=models.CASCADE)
    facebook_url = models.URLField(max_length=200,blank=True,null=True)
    instagram_url = models.URLField(max_length=200 ,blank=True,null=True)
    twtter_url = models.URLField(max_length=200,blank=True,null=True)
    linkdin_url = models.URLField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='service')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=StATUS)
    detaiil = models.TextField()

    def __str__(self):
        return self.name
    
