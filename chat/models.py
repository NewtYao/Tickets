#postgresql only

# from django.db import models
# from django.contrib.auth.models import User
# from website.models import Tickets

# class Room(models.Model):
#     room_name = models.ForeignKey(Tickets, related_name='ticket_chat', on_delete=models.CASCADE)
#     ticket_seller = models.ForeignKey(User, related_name='room_seller', on_delete=models.CASCADE)
#     buyer = models.ForeignKey(User, related_name='room_buyer', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.room_name

# class Message(models.Model):
#     chatroom = models.ForeignKey(Room, related_name='chat_message', on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.author.username} : {self.content}'
    
#     class Meta:
#         ordering = ['-created_at']

# Mongodb

from mongoengine import Document, ReferenceField, StringField, DateTimeField
from datetime import datetime
from website.models import Tickets  # Ensure this model is also in MongoDB

class Room(Document):
    room_name = StringField(required=True)  # Name or ID for the room
    ticket_seller = StringField()           # Stores ticket seller's user ID or username
    buyer = StringField()                   # Stores buyer's user ID or username

    def __str__(self):
        return self.room_name

class Message(Document):
    chatroom = ReferenceField(Room, required=True)  # References the `Room` document
    author = StringField(required=True)             # Stores author's user ID or username
    content = StringField(max_length=300, required=True)
    created_at = DateTimeField(default=datetime.utcnow)  # Set creation time

    def __str__(self):
        return f'{self.author}: {self.content[:50]}...'  # Displays a snippet of content

    meta = {
        'ordering': ['-created_at']  # Orders messages by most recent first
    }

