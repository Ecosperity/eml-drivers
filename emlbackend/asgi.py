import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import services.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emlbackend.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(services.routing.websocket_urlpatterns),
})