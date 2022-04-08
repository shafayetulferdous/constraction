from django.contrib import admin
from .models import Construction,ConstractionProjects

# Register your models here.
admin.site.register(ConstractionProjects)
admin.site.register(Construction)