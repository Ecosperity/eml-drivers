from django.urls import path
from services import views

urlpatterns = [
    path('driver/<int:fid>/', views.DriverList),
]