from http.client import HTTPResponse
from urllib import request
from .models import Driver
# from .serializers import DriverSerializer
# from rest_framework import generics
from django.views import View
from django.http import JsonResponse

# from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import JsonResponse

class DriverList(View):
  # search_fields = ['name', 'complaint']
  # filter_backends = (SearchFilter, filters.DjangoFilterBackend)
  # queryset = Driver.objects.all()
  # serializer_class = DriverSerializer

  def getData():
    set = Driver.objects.all()
    data = list(set.values())
    return JsonResponse(data, safe=False)