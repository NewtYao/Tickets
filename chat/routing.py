from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/chat/(?P<room_name>\d*+)/(?P<ticket_seller>\d*+)/(?P<buyer>\d*+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>[^/]+)/(?P<ticket_seller>[^/]+)/(?P<buyer>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]