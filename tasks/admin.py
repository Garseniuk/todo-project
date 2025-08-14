from django.contrib import admin
from .models import Task # Importujemy nasz model Task
# Register your models here.
admin.site.register(Task)