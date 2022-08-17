from .models import Driver
from .serializers import DriverSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io

def DriverApi(request):
  if (request.method == "GET"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    fid = python_data.get('id')
    if id is not None:
      data = Driver.objects.get(id=fid)
      serializer = DriverSerializer(data)
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