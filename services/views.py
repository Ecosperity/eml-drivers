from http.client import HTTPResponse
from urllib import request

from .serializers import DriverSerializer
from .models import Driver
# from .serializers import DriverSerializer
# from rest_framework import generics
from .forms import DriverForm
from django.views import View
from django.http import JsonResponse
from rest_framework import serializers
# from django.core.serializers.json import DjangoJSONEncoder

# from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import JsonResponse

# def getData():
#   set = Driver.objects.all()
#   data = list(set.values())
#   return JsonResponse(data, safe=False)

def addData(request):
  if request.method == "POST":
    fm = DriverForm(request.POST)
  else:
    fm = DriverForm()
  data = DriverSerializer(fm)
  return HTTPResponse(data)

# class DriverList(View):
  # search_fields = ['name', 'complaint']
  # filter_backends = (SearchFilter, filters.DjangoFilterBackend)
  # queryset = Driver.objects.all()
  # serializer_class = DriverSerializer

  # def getData():
  #   set = Driver.objects.all()
  #   data = list(set.values())
  #   return JsonResponse(data, safe=False)

  # def addData(request):
  #   if request.methd == "POST":
  #     fm = DriverForm(request.POST)
  #   else:
  #     fm = DriverForm()
  #   return JsonResponse(fm, safe=False)

# def GetAll(request):
#   d = Driver.objects.all()
#   data = list(d.values())
#   return JsonResponse(data, encoder=DjangoJSONEncoder, safe=False)

# def FilterById(request, fid):
#   d = Driver.objects.filter(id=fid)
#   data = list(d.values())
#   return JsonResponse(data, encoder=DjangoJSONEncoder, safe=False)