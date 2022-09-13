from .models import Registration, Complaints
from .serializers import RegisterSerializer, ComplaintSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
import json


def order(request , order_id):
    order = Complaints.objects.filter(order_id=order_id).first()
    json_data = json.dumps([dict(item) for item in order])
    return HttpResponse(json_data, content_type='application/json')
    # if order is None:
    #     return redirect('/')
    
    # context = {'order' : order}
    # return render(request , 'order.html', context)

# def order_pizza(request):
#     user = request.Name
#     data = json.loads(request.body)
    
#     try:
#         pizza =  Complaints.objects.get(id=data.get('id'))
#         order = Complaints(user=user, pizza=pizza , amount = pizza.price)
#         order.save()
#         return HttpResponse('Success', content_type='application/json')
        
#     except Complaints.DoesNotExist:
#         return HttpResponse('Failed', content_type='application/json')

def ComplaintApi(request):
  if (request.method == "GET"):
    json_data = json.dumps([dict(item) for item in Complaints.objects.values()])
    return HttpResponse(json_data, content_type='application/json')
  
  if (request.method == "POST"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = ComplaintSerializer(data=python_data)
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
      data = Complaints.objects.get(id=fid)
      serializer = ComplaintSerializer(data, data=python_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Updated Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    res = {'msg': 'Invalid Data'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')

  if (request.method == "PATCH"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    fid = python_data.get('id', None)
    if id is not None:
      data = Complaints.objects.get(id=fid)
      serializer = ComplaintSerializer(data, data=python_data, partial = True)
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
        data = Complaints.objects.get(id=fid)
      except Complaints.DoesNotExist:
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

def RegisterApi(request):
  if (request.method == "GET"):
    json_data = json.dumps([dict(item) for item in Registration.objects.values()])
    return HttpResponse(json_data, content_type='application/json')
  
  if (request.method == "POST"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = RegisterSerializer(data=python_data)
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
      data = Registration.objects.get(id=fid)
      serializer = RegisterSerializer(data, data=python_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Updated Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    res = {'msg': 'Invalid Data'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')
  
  if (request.method == "PATCH"):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    fid = python_data.get('id', None)
    if id is not None:
      data = Registration.objects.get(id=fid)
      serializer = RegisterSerializer(data, data=python_data, partial = True)
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
        data = Registration.objects.get(id=fid)
      except Registration.DoesNotExist:
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