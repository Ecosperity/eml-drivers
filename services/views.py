from django.shortcuts import render
from .models import Driver
from .serializers import DriverSerializer
from rest_framework import generics

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



def DriverList(fid):
  search_fields = ['name', 'complaint']
  filter_backends = (SearchFilter, filters.DjangoFilterBackend)
  queryset = Driver.objects.filter(id = fid)
  serializer_class = DriverSerializer