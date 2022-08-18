from rest_framework import serializers
from .models import Registration

class DriverSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = '__all__'
    
def update(self, instance, validated_data):
  instance.Name = validated_data.get('id', instance.id)
  instance.Age = validated_data.get('name', instance.name)
  instance.State = validated_data.get('complaint', instance.complaint)
  instance.City = validated_data.get('id', instance.id)
  instance.phoneNo = validated_data.get('name', instance.name)
  instance.Language = validated_data.get('complaint', instance.complaint)
  instance.DoM = validated_data.get('id', instance.id)
  instance.DoR = validated_data.get('name', instance.name)
  instance.DoIns = validated_data.get('complaint', instance.complaint)
  instance.InsDuration = validated_data.get('id', instance.id)
  instance.nChassisNoame = validated_data.get('name', instance.name)
  instance.modelNo = validated_data.get('complaint', instance.complaint)
  instance.save()
  return instance
