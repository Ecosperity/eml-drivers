from http.client import HTTPResponse
from urllib import request
from .models import Driver
from .serializers import DriverSerializer
from rest_framework import generics
from django.views import View
from django.http import JsonResponse

from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import JsonResponse

# def getData(request):
#   set = Driver.objects.all()
#   data = list(set.values())
#   return JsonResponse(data, safe=False)

class DriverList(generics.ListCreateAPIView):
  search_fields = ['name', 'complaint']
  filter_backends = (SearchFilter, filters.DjangoFilterBackend)
  queryset = Driver.objects
  serializer_class = DriverSerializer

  def get(self, request, *args, **kwargs):
    data = list(self.queryset.all().values())
    return JsonResponse(data, safe=False)

  # def delete(self, request, *args, **kwargs):
