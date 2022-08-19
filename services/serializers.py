from rest_framework import serializers
from .models import Registration, Complaints

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = '__all__'
  
  def update(self, instance, validated_data):
    instance.Name = validated_data.get('Name', instance.Name)
    instance.Age = validated_data.get('Age', instance.Age)
    instance.State = validated_data.get('State', instance.State)
    instance.City = validated_data.get('City', instance.City)
    instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
    instance.Language = validated_data.get('Language', instance.Language)
    instance.DoM = validated_data.get('DoM', instance.DoM)
    instance.DoR = validated_data.get('DoR', instance.DoR)
    instance.DoIns = validated_data.get('DoIns', instance.DoIns)
    instance.InsDuration = validated_data.get('InsDuration', instance.InsDuration)
    instance.ChassisNo = validated_data.get('ChassisNo', instance.ChassisNo)
    instance.modelNo = validated_data.get('modelNo', instance.modelNo)
    instance.save()
    return instance


class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaints
    fields = '__all__'

  def update(self, instance, validated_data):
    instance.Name = validated_data.get('Name', instance.Name)
    instance.City = validated_data.get('City', instance.City)
    instance.Ticket = validated_data.get('Ticket', instance.Ticket)
    instance.Subject = validated_data.get('Subject', instance.Subject)
    instance.Status = validated_data.get('Status', instance.Status)
    instance.Time = validated_data.get('Time', instance.Time)
    instance.VID = validated_data.get('VID', instance.VID)
    instance.Progress = validated_data.get('Progress', instance.Progress)
    instance.save()
    return instance