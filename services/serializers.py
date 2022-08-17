from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
  class Meta:
    model = Driver
    fields = '__all__'

    def update(self, instance, validated_data):
      instance.id = validated_data.get('id', instance.id)
      instance.name = validated_data.get('name', instance.name)
      instance.complaint = validated_data.get('complaint', instance.complaint)
      instance.save()
      return instance
