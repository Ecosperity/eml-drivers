from django.urls import path
from services import views

urlpatterns = [
    path('driver/', views.DriverList.getData()),
]