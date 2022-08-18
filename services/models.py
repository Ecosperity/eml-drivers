from django.db import models


class Registration(models.Model):
  Name = models.CharField(max_length=30)
  Age = models.PositiveIntegerField(default=0)
  State = models.CharField(max_length=30)
  City = models.CharField(max_length=30)
  phoneNo = models.CharField(max_length=20)
  Language = models.CharField(max_length=30)
  DoM = models.CharField(max_length=30)
  DoR = models.CharField(max_length=30)
  DoIns = models.CharField(max_length=30)
  InsDuration = models.PositiveIntegerField(default=0)
  ChassisNo = models.CharField(max_length=30)
  modelNo = models.CharField(max_length=30)

