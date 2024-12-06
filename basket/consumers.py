from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BasketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'basket_updates'

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_update(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))



from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def add_to_basket(request):
    # Your basket logic
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'basket_updates',
        {
            'type': 'basket_update',
            'message': 'A new item was added to the basket!',
        }
    )
