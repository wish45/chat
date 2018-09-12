# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat_app.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(     #websocket은 AuthMiddlewareStack에서 처리할 수 있도록 scope를 지정한다.
        URLRouter(
            chat_app.routing.websocket_urlpatterns
        )
    ),
})

#chat앱에서 routing파일을 장고가 인식할 수 있도록  urlRouter를 넣어준다.
#http를 정의하지 않을경우는 장고뷰 시스템의 asgi인터페이스인 channels.http.asgihandler가 기본적으로 처리한다:
