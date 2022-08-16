from django.urls import path
from services import views

urlpatterns = [
    path('getall', views.DriverList.as_view()),

    # path('getall', views.GetAll),
    # path('getone/<fid>', views.FilterById),
]