"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chat_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('room/', views.room, name='room'),
    # path('<int:room_label>/chat/<name>', views.chat, name='chat'), #전체 채팅
    path('<user>/chat/<target_name>', views.one_chat, name='one_chat'), #1to1 채팅
    path('<str:user>/onechat/<room_label>/<str:target_name>', views.singlechat, name='singlechat'),

    path('accounts/', include('accounts.urls')), #accounts path
]

if settings.DEBUG == True:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)









