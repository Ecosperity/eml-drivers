from django.shortcuts import render
from .models import Driver
from .serializers import DriverSerializer
# from rest_framework.generics import ListAPIView
from rest_framework import generics, filters


class DriverList(generics.ListCreateAPIView):
  search_fields = ['name', 'complaint']
  filter_backends = (filters.SearchFilter)
  queryset = Driver.objects.all()
  serializer_class = DriverSerializer