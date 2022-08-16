from django.urls import path
from services.views import DriverList

urlpatterns = [
    path('driver/', DriverList.as_view()),
]