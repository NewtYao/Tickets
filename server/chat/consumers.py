import json

from .models import Message, Room
from .views import chat_room
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('check try connect')
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.ticket_seller = self.scope["url_route"]["kwargs"]["ticket_seller"]
        self.buyer = self.scope["url_route"]["kwargs"]["buyer"]
        self.room_group_name = f"chat_{self.room_name}"
        print('check connect room')
        print(self.room_group_name)
        print(self.room_name)
        print(self.buyer)
        print(self.ticket_seller)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print('check disconnect room')

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)
        print('receive from websocket')
        user = self.scope['user']
        print(user)
        print(user.id)
        print(self.ticket_seller)
        print(self.room_name)
        chatroom = await sync_to_async(Room.objects.get)(
            room_name_id=self.room_name,
            ticket_seller_id=self.ticket_seller,
            buyer_id=user,
            )
        print('chatroom pass')
        async def save_message(message, user, chatroom):
            print('start save message')
            print(message)
            print(user)
            # print(chatroom)
            new_message = await sync_to_async (Message.objects.create)(
                content=message,
                author=user,
                chatroom=chatroom,)
            print('check new message')
            message_data = {
                'message': new_message.content,
                'author': new_message.author.username
            }
            return message_data 
            # return new_message
        new_message = await save_message(message, user, chatroom)
        print(new_message)

        

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': new_message  # Send the entire message object
            }
        )
            # 'type': 'chat.message',
            # 'message': new_message.content,
            # 'message': new_message.message,
            # 'author': new_message.author}
            # 'author': new_message.author.username}
        print('send to room')

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # author_name = event.get("author")
        print(message)


        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        print('send message to room')
        print(message)