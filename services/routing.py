from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('<order_id>', consumers.OrderProgress.as_asgi())
]