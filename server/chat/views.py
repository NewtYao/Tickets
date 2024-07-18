from django.shortcuts import render
from django.contrib.auth.models import User

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Room

# chat/views.py

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
