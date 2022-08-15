from .models import Driver
from .serializers import DriverSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class DriverList(ListAPIView):
  queryset = Driver.objects.all()
  serializer_class = DriverSerializer