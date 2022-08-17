from .models import Driver
from .serializers import DriverSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io

def DriverApi(request):
  # if (request.method == "GET"):
  #   json_data = request.body
  #   stream = io.BytesIO(json_data)
  #   python_data = JSONParser().parse(stream)
  #   fid = python_data.get('id')
  #   if id is not None:
  #     data = Driver.objects.get(id=fid)
  #     serializer = DriverSerializer(data)
  #     json_data = JSONRenderer().render(serializer.data)
  #     return HttpResponse(json_data, content_type='application/json')

  if (request.method == "GET"):
    data = Driver.objects.get.all()
    data_list = list(data.values())
    serializer = DriverSerializer(data_list)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
  
  if (request.method == "POST"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = DriverSerializer(data=python_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Created Successfully'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    return HttpResponse(JSONRenderer().render(serializer.errors), content_type='application/json')

  if (request.method == "PUT"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    fid = python_data.get('id', None)
    if id is not None:
      data = Driver.objects.get(id=fid)
      serializer = DriverSerializer(data, data=python_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Updated Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    res = {'msg': 'Invalid Data'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')

  
  if (request.method == "DELETE"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    fid = python_data.get('id', None)
    if id is not None:
      try:
        data = Driver.objects.get(id=fid)
      except Driver.DoesNotExist:
        res = {'msg': 'Data does not exsit'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
      data.delete()
      res = {'msg': 'Data Deleted Successfully'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    res = {'msg': 'Please provide Id to Delete'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')