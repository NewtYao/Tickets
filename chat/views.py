# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

# import json
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST

# from .models import *
# from .forms import *
# from website.models import Tickets

# # chat/views.py


# @login_required
# def chat_room(request, room_name, ticket_seller, buyer):
#     try:
#         chat_room_curr = get_object_or_404(Room, room_name_id=room_name, ticket_seller_id=ticket_seller, buyer_id=buyer)
#     except:
#         chat_room_curr = Room.objects.create(room_name_id=room_name, ticket_seller_id=ticket_seller, buyer_id=buyer)
#     chat_message_curr = chat_room_curr.chat_message.all()[:30]
#     form = ChatMessageCreateForm()

#     return render(request, "chat/chat_room.html", {'chat_message_curr' : chat_message_curr, 'form' : form, 'room_name': room_name, 'ticket_seller':ticket_seller, 'buyer':buyer})

# @login_required
# def chat_list(request):
#     user_id = request.user.id
#     sell_chatroom_lists = Room.objects.filter(ticket_seller_id=user_id).prefetch_related('buyer')
#     buy_chatroom_lists = Room.objects.filter(buyer_id=user_id)
#     return render(request, "chat/chat_list.html", {'selling':sell_chatroom_lists, 'buying':buy_chatroom_lists})

# Mongodb one

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Room, Message  # Import MongoEngine models
from .forms import ChatMessageCreateForm
from website.models import Tickets

# chat/views.py

@login_required
def chat_room(request, room_name, ticket_seller, buyer):
    # Ensure we have the correct IDs for room_name, ticket_seller, and buyer
    ticket = get_object_or_404(Tickets, id=room_name)
    seller = get_object_or_404(User, id=ticket_seller)
    buyer_user = get_object_or_404(User, id=buyer)

    # Check if a room exists with the given parameters in MongoDB
    chat_room_curr = Room.objects(room_name=str(ticket.id), ticket_seller=str(seller.id), buyer=str(buyer_user.id)).first()
    if not chat_room_curr:
        # Create the chat room if it doesn't exist
        chat_room_curr = Room(room_name=str(ticket.id), ticket_seller=str(seller.id), buyer=str(buyer_user.id))
        chat_room_curr.save()

    # Get the latest 30 messages in the chat room
    chat_message_curr = Message.objects(chatroom=chat_room_curr).order_by('-created_at')[:30]

    print(f"Messages: {list(chat_message_curr)}")
    
    # Initialize the form
    form = ChatMessageCreateForm()

    return render(request, "chat/chat_room.html", {
        'chat_message_curr': chat_message_curr,
        'form': form,
        'room_name': room_name,
        'ticket_seller': ticket_seller,
        'buyer': buyer,
    })

@login_required
def chat_list(request):
    user_id = str(request.user.id)  # Get the current user's ID as a string

    # Retrieve rooms where the user is either the ticket seller or the buyer
    sell_chatroom_lists = Room.objects(ticket_seller=user_id)
    buy_chatroom_lists = Room.objects(buyer=user_id)

    for room in sell_chatroom_lists:
        print(f"Sell Room: {room.room_name}, {room.ticket_seller}, {room.buyer}")
    for room in buy_chatroom_lists:
        print(f"Buy Room: {room.room_name}, {room.ticket_seller}, {room.buyer}")


    selling = []
    for room in sell_chatroom_lists:
        selling.append({
            'room_name': room.room_name,
            'ticket_seller': User.objects.get(id=room.ticket_seller),
            'buyer': User.objects.get(id=room.buyer)
        })

    buying = []
    for room in buy_chatroom_lists:
        buying.append({
            'room_name': room.room_name,
            'ticket_seller': User.objects.get(id=room.ticket_seller),
            'buyer': User.objects.get(id=room.buyer)
        })

    return render(request, "chat/chat_list.html", {
        'selling': selling,
        'buying': buying,
    })
