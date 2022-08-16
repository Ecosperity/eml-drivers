from django.urls import path
from services import views

urlpatterns = [
<<<<<<< HEAD
    path('driver/<fid>', views.DriverList),
=======
    path('driver/<int:fid>/', views.DriverList),
>>>>>>> 8ba042104cfe52cdbe2d3362b82d7a8bbd6ec285
]