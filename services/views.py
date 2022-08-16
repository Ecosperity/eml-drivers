from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from .models import Driver
from .serializers import DriverSerializer
from rest_framework import generics

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



# class DriverList(generics.ListCreateAPIView):
#   search_fields = ['name', 'complaint']
#   filter_backends = (SearchFilter, filters.DjangoFilterBackend)
#   queryset = Driver.objects.all()
#   serializer_class = DriverSerializer


def DriverList(request):
  d = Driver.objects.all()
  return render(request, 'service/', {'driver': d})
