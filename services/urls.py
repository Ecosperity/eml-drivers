from django.urls import path
from services import views

urlpatterns = [
    path('driver/', views.RegisterApi),
    path('complaint/', views.ComplaintApi),
    path('<order_id>/', views.order),
]