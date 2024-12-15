from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path("<int:room_name>/<int:ticket_seller>/<int:buyer>/", views.chat_room, name='chat_room'),
    path("chat_list/", views.chat_list, name='chat_list'),
]