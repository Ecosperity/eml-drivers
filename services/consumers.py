from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from .models import *

# class CompConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name='Complaint Data'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()
    
#     async def disconnect(self,close_code):
#         pass

#     async def receive(self,text_data):
#         # print (text_data)
#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type':'send_order',
#                 'value':text_data,
#             }
#         )

#     async def send_order(self,event):
#         print (event['value'])
#         await self.send(event['value'])

class mySock(WebsocketConsumer):
    def connect(self):
        self.room_name = 'EML'
        self.room_group_name = 'EML ROOM'
        self.accept()
        self.send(
            text_data=json.dumps({'status': 'Connected to Socket'})
        )
        
    def receive(self, text_data):
        print(text_data)
        self.send(
            text_data=json.dumps({'status': 'We got you'})
        )

    def disconnect(self, code):
        pass