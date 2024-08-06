from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # path("", views.index, name="index"),
    path("<str:room_name>/<str:ticket_seller>/<str:buyer>/", views.chat_room, name='chat_room'),
]