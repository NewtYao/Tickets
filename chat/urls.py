from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path("<str:room_name>/<str:ticket_seller>/<str:buyer>/", views.chat_room, name='chat_room'),
    path("chat_list/", views.chat_list, name='chat_list'),
]