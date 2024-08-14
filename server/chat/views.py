from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import *
from .forms import *
from website.models import Tickets

# chat/views.py


@login_required
def chat_room(request, room_name, ticket_seller, buyer):
    try:
        chat_room_curr = get_object_or_404(Room, room_name_id=room_name, ticket_seller_id=ticket_seller, buyer_id=buyer)
    except:
        chat_room_curr = Room.objects.create(room_name_id=room_name, ticket_seller_id=ticket_seller, buyer_id=buyer)
    chat_message_curr = chat_room_curr.chat_message.all()[:30]
    form = ChatMessageCreateForm()

    return render(request, "chat/chat_room.html", {'chat_message_curr' : chat_message_curr, 'form' : form, 'room_name': room_name, 'ticket_seller':ticket_seller, 'buyer':buyer})

@login_required
def chat_list(request):
    user_id = request.user.id
    sell_chatroom_lists = Room.objects.filter(ticket_seller_id=user_id).prefetch_related('room_buyer')
    buy_chatroom_lists = Room.objects.filter(buyer_id=user_id)
    return render(request, "chat/chat_list.html", {'selling':sell_chatroom_lists, 'buying':buy_chatroom_lists})