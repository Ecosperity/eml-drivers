from django.db import models


class Registration(models.Model):
  Name = models.CharField(max_length=30)
  Age = models.CharField(max_length=4)
  State = models.CharField(max_length=30)
  City = models.CharField(max_length=30)
  phoneNo = models.CharField(max_length=20)
  Language = models.CharField(max_length=30)
  DoM = models.CharField(max_length=30)
  DoR = models.CharField(max_length=30)
  DoIns = models.CharField(max_length=30)
  InsDuration = models.CharField(max_length=4)
  ChassisNo = models.CharField(max_length=30)
  modelNo = models.CharField(max_length=30)

class Complaints(models.Model):
  Name = models.CharField(max_length=30)
  City = models.CharField(max_length=30)
  Ticket = models.CharField(max_length=30)
  Subject = models.CharField(max_length=30)
  Status = models.CharField(max_length=30)
  Time = models.CharField(max_length=30)
  VID = models.CharField(max_length=30)
  Progress = models.CharField(max_length=30)
