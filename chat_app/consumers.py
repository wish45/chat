#channels 1.1.8, asgiref 1.1.2 version
# from channels import Group
#
# def ws_add(message):
# 	print('add')
# 	message.reply_channel.send({'accept':True})
# 	Group('chat').add(message.reply_channel)
#
# def ws_message(message):
# 	print('message:{}'.format(message.content['text']))
# 	Group('chat').send({'text': message.content['text']})
#
# def ws_disconnect(message):
# 	print('disconnect')
# 	Group('chat').discard(message.reply_channel)
from builtins import property

from channels.generic.websocket import AsyncWebsocketConsumer
import json

from django.shortcuts import get_object_or_404, render

from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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
        print("?????????????????")
        print(text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['mensaje']
        nombre = text_data_json['nombre']
        room_name = text_data_json["room_name"]

        print("룸찾기시작")
        room = Room.objects.get(pk=room_name)
        print("채팅내용저장시작")
        room.messages.create(userId=nombre, message=message)
        print("저장끝")


        # Send message to room group
        await self.channel_layer.group_send(
        self.room_group_name,
            {
                'type': 'chat_message',
                'nombre':nombre,
                'message': message,
                'room_name': room_name,
            }
         )

    # Receive message from room group
    async def chat_message(self, event):
        print(event)
        message = event['message']
        nombre = event['nombre']
        room_name = int(event['room_name'])
        print(nombre)
        print(room_name)
        print(message)
        # print("룸찾기시작")
        # room = Room.objects.get(pk=room_name)
        # print("룸찾기완료 및 메시지 생성시작")
        # room.messages.create(userId=nombre, message=message)
        #
        # print("메시지 생성 완료")
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'mensaje': message,
            'nombre':nombre,
            'room_name':room_name,
        }))
        print("끝")




