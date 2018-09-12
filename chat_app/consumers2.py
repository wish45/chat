from builtins import property

from channels.generic.websocket import AsyncWebsocketConsumer
import json

from django.shortcuts import get_object_or_404, render

from .models import Room, Message, Oneroom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_label = self.scope['url_route']['kwargs']['room_label']
        self.room_group_name = 'chat_%s' % self.room_label

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data): #socket.send json타입으로 전달해줘서 text_data로 받나봄...
        print("웹소켓에서 리시브받음")
        print("텍스트 데이타")
        print(text_data)

        text_data_json = json.loads(text_data)

        user = text_data_json['user']
        message = text_data_json['mensaje']
        room_label = text_data_json["room_label"]

        room = Oneroom.objects.get(pk=room_label)
        room.onemessages.create(userId=user, message=message)
        print("저장끝")

        # Send message to room group
        await self.channel_layer.group_send(
        self.room_group_name,
            {
                'type': 'chat_message',
                'nombre':user,
                'message': message,
                'room_label': room_label,
            }
         )

    # Receive message from room group
    async def chat_message(self, event):
        print("룸 그룹으로부터 메시지 받음")
        print("이벤트")
        print(event)
        message = event['message']
        nombre = event['nombre']
        room_label = int(event['room_label'])

        await self.send(text_data=json.dumps({
            'mensaje': message,
            'nombre':nombre,
            'room_label':room_label,
        }))
        print("끝")


