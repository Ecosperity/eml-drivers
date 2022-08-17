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
    id = python_data.get('id')
    if id is not None:
      data = Driver.objects.get(id=id)
      serializer = DriverSerializer(set)
      json_data = JSONRenderer().render(serializer.data)
      return HttpResponse(json_data, content_type='application/json')