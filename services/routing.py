from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('test', consumers.mySock.as_asgi())
    path('comp', consumers.CompConsumer.as_asgi())
]