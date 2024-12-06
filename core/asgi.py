import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from basket import routing  # routing faylni chaqiring

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP so'rovlar
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # WebSocket marshrutlari
        )
    ),
})
