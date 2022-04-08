from django.db import models

# Create your models here.
class Construction(models.Model):
    status = (
        ('True','True'),
        ('False','False'),

    )
 

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=50)
    details = models.TextField()
    image = models.ImageField(blank=True,upload_to='categories')
    slug = models.SlugField(unique=True,null=True)
    status = models.CharField(max_length=100,choices=status)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    
class ConstractionProjects(models.Model):
    status = (
        ('True','True'),
        ('False','False'),)
    category = models.ForeignKey(Construction,on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

 


