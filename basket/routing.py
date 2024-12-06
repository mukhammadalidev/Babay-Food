from django.urls import path
from .consumers import BasketConsumer

websocket_urlpatterns = [
    path('ws/basket/', BasketConsumer.as_asgi()),
]
