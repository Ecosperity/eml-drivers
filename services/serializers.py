from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.Serializer):
  class Meta:
    model = Driver
    fields = '__all__'