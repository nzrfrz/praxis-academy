from django.contrib import admin
from . models import Registration 

# Register your models here.
class RegistartionForADmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']

admin.site.register(Registration, RegistartionForADmin)
