from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import *
from .forms import *

# chat/views.py


@login_required
def chat_room(request, room_name):
    chat_room_curr = get_object_or_404(Room, room_name_id=room_name)
    chat_message_curr = chat_room_curr.chat_message.all()[:30]
    form = ChatMessageCreateForm()
    print('pass through')

    # if request.method == "POST":
    #     form = ChatMessageCreateForm(request.POST)
    #     if form.is_valid():
    #         print('check views')
    #         message = form.save(commit=False)
    #         message.author = request.user
    #         message.chatroom = chat_room_curr
    #         message.save()
    #         return redirect('chat:chat_room', room_name=room_name)

    return render(request, "chat/chat_room.html", {'chat_message_curr' : chat_message_curr, 'form' : form, 'room_name': room_name})
