# import json
# from .models import Message, Room
# from .views import chat_room
# from asgiref.sync import sync_to_async
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.ticket_seller = self.scope["url_route"]["kwargs"]["ticket_seller"]
#         self.buyer = self.scope["url_route"]["kwargs"]["buyer"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         user = self.scope['user']
#         if int(self.ticket_seller) == int(user.id):
#             buyer_name=self.scope["url_route"]["kwargs"]["buyer"]
#             chatroom = await sync_to_async(Room.objects.get)(
#                 room_name_id=self.room_name,
#                 ticket_seller_id=self.ticket_seller,
#                 buyer_id = buyer_name,
#             )
#         else:
#             chatroom = await sync_to_async(Room.objects.get)(
#                 room_name_id=self.room_name,
#                 ticket_seller_id=self.ticket_seller,
#                 buyer_id=user,
#                 )
#         async def save_message(message, user, chatroom):
#             new_message = await sync_to_async (Message.objects.create)(
#                 content=message,
#                 author=user,
#                 chatroom=chatroom,)
#             message_data = {
#                 'message': new_message.content,
#                 'author': new_message.author.username
#             }
#             return message_data 
#         new_message = await save_message(message, user, chatroom)

        

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat.message',
#                 'message': new_message  # Send the entire message object
#             }
#         )


#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))

# Mongodb 

# import json
# from .models import Message, Room  # MongoEngine models
# from asgiref.sync import sync_to_async
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.ticket_seller = self.scope["url_route"]["kwargs"]["ticket_seller"]
#         self.buyer = self.scope["url_route"]["kwargs"]["buyer"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         user = self.scope['user']

#         # Determine buyer ID based on ticket seller
#         if int(self.ticket_seller) == int(user.id):
#             buyer_id = self.buyer  # Use buyer from URL if user is ticket seller
#         else:
#             buyer_id = str(user.id)  # Use the user's ID if they are not the ticket seller

#         # Get or create the chatroom using sync_to_async for MongoEngine compatibility
#         chatroom = await sync_to_async(self.get_or_create_room)(self.room_name, self.ticket_seller, buyer_id)

#         # Save the message and get message data
#         new_message = await sync_to_async(self.save_message)(message, user, chatroom)

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat.message',
#                 'message': new_message['message'],  # Send only content
#                 'author': new_message['author']      # Send author too
#             }
#         )

#     def get_or_create_room(self, room_name, ticket_seller, buyer):
#         # Retrieve room or create a new one if it doesn’t exist
#         # chatroom, created = Room.objects.get_or_create(
#         #     room_name=str(room_name),
#         #     ticket_seller=str(ticket_seller),
#         #     buyer=str(buyer)
#         # )
#         chatroom = Room.objects(room_name=str(room_name), ticket_seller=str(ticket_seller), buyer=str(buyer)).first()
#         if not room:
#             room = Room(room_name=str(room_name), ticket_seller=str(ticket_seller), buyer=str(buyer))
#             room.save()
#         return chatroom

#     def save_message(self, content, user, chatroom):
#         # Save the message in the chatroom with MongoEngine
#         new_message = Message(
#             content=content,
#             author=str(user.id),  # Store the user's ID as a string
#             chatroom=chatroom
#         )
#         new_message.save()

#         # Prepare the message data to send back to the WebSocket
#         message_data = {
#             'message': new_message.content,
#             'author': user.username  # Assuming user has a username attribute
#         }
#         return message_data

#     async def chat_message(self, event):
#         message = event["message"]
#         author = event["author"]

#         # Send message to WebSocket with author information
#         await self.send(text_data=json.dumps({"message": message, "author": author}))


import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Room  # MongoEngine models

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.ticket_seller = self.scope["url_route"]["kwargs"]["ticket_seller"]
        self.buyer = self.scope["url_route"]["kwargs"]["buyer"]
        self.room_group_name = f"chat_{self.room_name}"

        if not self.scope["user"].is_authenticated:
            await self.close()
            return

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope['user']

        # Determine buyer ID based on ticket seller
        if int(self.ticket_seller) == int(user.id):
            buyer_id = self.buyer
        else:
            buyer_id = str(user.id)

        # Get or create the chatroom
        chatroom = await sync_to_async(self.get_or_create_room)(self.room_name, self.ticket_seller, buyer_id)

        # Save the message
        new_message = await sync_to_async(self.save_message)(message, user, chatroom)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': new_message['message'],
                'author': new_message['author']
            }
        )

    def get_or_create_room(self, room_name, ticket_seller, buyer):
        room = Room.objects(room_name=str(room_name), ticket_seller=str(ticket_seller), buyer=str(buyer)).first()
        if not room:
            room = Room(room_name=str(room_name), ticket_seller=str(ticket_seller), buyer=str(buyer))
            room.save()
        return room

    def save_message(self, content, user, chatroom):
        new_message = Message(
            content=content,
            author=str(user.username),
            chatroom=chatroom
        )
        new_message.save()

        return {
            'message': new_message.content,
            'author': new_message.author,
        }

    async def chat_message(self, event):
        message = event["message"]
        author = event["author"]

        await self.send(text_data=json.dumps({"message": message, "author": author}))
