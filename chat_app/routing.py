#channels 1 version
# from channels.routing import route
# from chat_app import consumers
#
# channel_routing = [
# 	route('websocket.connect', 		consumers.ws_add,			path=r'^/chat/$'),
# 	route('websocket.receive', 		consumers.ws_message,		path=r'^/chat/$'),
# 	route('websocket.disconnect',	consumers.ws_disconnect, 	path=r'^/chat/$'),
# ]
#







from django.conf.urls import url

from . import consumers, consumers2

#소비자 라우팅을 처리하기 위해 chat 앱에 있는 routing configuration 파일을 생성한다.
websocket_urlpatterns = [
    url(r'^ws/chat/one/(?P<room_label>[^/]+)/$', consumers2.ChatConsumer), #일대일채팅
    #url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer), #다대다채팅
]






