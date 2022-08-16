from django.urls import path
from services import views

urlpatterns = [
    path('driver/<id>/', views.DriverList.as_view()),
]