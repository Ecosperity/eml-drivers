from django.contrib import admin
from .models import Registration

# Register your models here.
@admin.register(Registration)
class DriverAdmin(admin.ModelAdmin):
  list_display = ['Name', 'Age', 'State','City', 'phoneNo', 'Language','DoM', 'DoR', 'DoIns','InsDuration', 'ChassisNo', 'modelNo',]