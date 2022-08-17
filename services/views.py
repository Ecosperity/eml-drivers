# from urllib import request
from .models import Driver
from .serializers import DriverSerializer
# from rest_framework import generics
# from django.views import View
# from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import JsonResponse

def getData(request):
  set = Driver.objects.get(id=1)
  serializer = DriverSerializer(set)
  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data, content_type='application/json')
  # data = list(set.values())
  # return JsonResponse(data, safe=False)

# class DriverList(generics.ListCreateAPIView):
#   search_fields = ['name', 'complaint']
#   filter_backends = (SearchFilter, filters.DjangoFilterBackend)
#   queryset = Driver.objects
#   serializer_class = DriverSerializer

#   def get(self, request, *args, **kwargs):
#     data = list(self.queryset.all().values())
#     return JsonResponse(data, safe=False)

#   def delete(self, request, fid, *args, **kwargs):
#     data = list(self.queryset.filter(id=fid).values())
#     return JsonResponse(data, safe=False)