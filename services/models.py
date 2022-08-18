from tokenize import Name
from django.db import models

# Create your models here.
class VehicleManager(models.Manager): 
  def Register(self):
    return self

class Registration(models.Model):
  Name = models.CharField(max_length=30)
  Age = models.PositiveIntegerField
  State = models.CharField(max_length=30)
  City = models.CharField(max_length=30)
  phoneNo = models.CharField(max_length=20)
  Language = models.CharField(max_length=30)
  DoM = models.CharField(max_length=30)
  DoR = models.CharField(max_length=30)
  DoIns = models.CharField(max_length=30)
  InsDuration = models.PositiveIntegerField
  ChassisNo = models.CharField(max_length=30)
  modelNo = models.CharField(max_length=30)

  objects = VehicleManager()

