from django.urls import path
from services import views

urlpatterns = [
    path('driver/', views.DriverList.as_view()),
    path('driverd/<fid>/', views.DriverList.as_view()),
]