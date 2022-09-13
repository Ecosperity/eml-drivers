from django.db import models
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
import json
import random
from channels.layers import get_channel_layer


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
  complaint_id = models.CharField(max_length=100 , blank=True)
  Name = models.CharField(max_length=30)
  City = models.CharField(max_length=30)
  Ticket = models.CharField(max_length=30)
  Subject = models.CharField(max_length=30)
  Status = models.CharField(max_length=30)
  Time = models.CharField(max_length=30)
  VID = models.CharField(max_length=30)
  Progress = models.CharField(max_length=30)

  def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

  def save(self, *args, **kwargs):
    if not len(self.complaint_id): self.complaint_id = Complaints.random_string_generator()
    super(Complaints, self).save(*args, **kwargs)

  @staticmethod
  def give_order_details(complaint_id):
    instance = Complaints.objects.filter(complaint_id=complaint_id).first()
    data  = {}
    data['complaint_id'] = instance.complaint_id
    data['Status'] = instance.Status
    progress_percentage = 20
    if instance.status == 'Order Recieved':
      progress_percentage = 20
    elif instance.status == 'Baking':
      progress_percentage = 40
    elif instance.status == 'Baked':
      progress_percentage = 60
    elif instance.status == 'Out for delivery':
      progress_percentage = 80
    elif instance.status == 'Order recieved':
      progress_percentage = 100
            
    data['progress'] = progress_percentage
        
    return data
        
    
    def __str__(self):
      return self.complaint_id


@receiver(post_save, sender=Complaints)
def order_status_handler(sender, instance,created , **kwargs):
    
    if not created:
        print("###################")
        channel_layer = get_channel_layer()
        data  = {}
        data['complaint_id'] = instance.complaint_id
        data['Status'] = instance.Status
        progress_percentage = 20
        if instance.status == 'Order Recieved':
            progress_percentage = 20
        elif instance.status == 'Baking':
            progress_percentage = 40
        elif instance.status == 'Baked':
            progress_percentage = 60
        elif instance.status == 'Out for delivery':
            progress_percentage = 80
        elif instance.status == 'Order recieved':
            progress_percentage = 100
    
        
        data['progress'] = progress_percentage
        async_to_sync(channel_layer.group_send)(
            'order_%s' % instance.complaint_id,{
                'type': 'order_status',
                'value': json.dumps(data)
            }
        )
