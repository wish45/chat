import json

from django.contrib.auth.decorators import login_required

from .models import Room, Oneroom
from django.contrib.auth import get_user_model
from .models import Message
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q

from django.utils.safestring import mark_safe


def home(request):
    return render(request, 'chat_app/index.html')

@login_required
def room(request):
    rooms = Room.objects.all()
    onerooms = Oneroom.objects.all() #방만들어져 있는거 가져오기
    #nombre = request.POST.get('userName') #기존 아이디 입력받는곳
    nombre = request.POST.get('user')
    print("else chat views ")

    user = get_user_model()
    userList = user.objects.exclude(username=request.user)
    context = {
        'nombre': nombre, #name이 user인것을 가져와서 nombre로 넘겨줌.
        'rooms': rooms, #model에 있는 room객체들을 다 가져와서 넘겨줌.
        'userList': userList, #로그인한 유저를 제외한 나머지 유저들 리스트
        'onerooms': onerooms, #만들어져 있는 모든 방 가져옴.
    }
    return render(request, 'chat_app/room.html', context)

@login_required
def chat(request, room_label, name) :
    #여기 room_name안써줫더니 TypeError: chat() got an unexpected keyword argument 'room_name'
    #이런 에러 발생했다.
    print("멍미?")
    #nombre = request.GET.get('hoho') #폼태그 안에 name값(value)을 가져온다.

    room_inside = Room.objects.get(label=room_label)
    #chat_inside = Message.objects.get(all)
    msg_list = room_inside.messages.all()


    nombre=name
    print(nombre)


    return render(request, 'chat_app/chat.html', {
        #'room_name_json': mark_safe(json.dumps(room_name)),
        'room_inside': room_inside,
        'nombre':nombre,
        'msg_list': msg_list,
        'room_name':mark_safe(json.dumps(room_label)), #이렇게 안해주면 스크립트 코드 내에서 var roomName ={{ room_name }};이거 인식못함.
    })


#일대일채팅 유저목록
@login_required
def one_chat(request, user, target_name):
    users = get_user_model() #유저모델
    user1 = users.objects.get(username=user) #로그인한유저
    user2 = users.objects.get(username=target_name) #타겟유저
    onerooms = Oneroom.objects.filter(users=user1) #user1유저를 가져옴
    flag = 0
    for oneroom in onerooms:
        for userss in oneroom.users.all():
            if userss.pk is user2.pk:
               flag = 1
    print("flag는 {}".format(flag))
    if flag == 0:
        oneroom = Oneroom.objects.create()
        oneroom.save()
        oneroom.users.add(user1, user2)

    userr = user
    specifics = Oneroom.objects.filter(users__username=target_name)
    print("일대일 채팅 유저 리스트")
    print(specifics)
    return render(request, 'chat_app/chatuserlist.html',{
        'userr': userr,
        'target_name':target_name,
        'specifics':specifics,
    })


#기존
# @login_required
# def one_chat(request, user, target_name):
#     print("일대일 채팅 view")
#     return render(request, 'chat_app/onechat.html',{
#         #'user':mark_safe(json.dumps(user)),
#         'user': user,
#         'target_name':target_name,
#     })




# request.POST.get('name',default=None).- namePOST 요청에서 매개 변수 의
# 값을 가져 오거나 None매개 변수가없는 경우 가져 옵니다.
# 메모 default는 사용자 지정 값으로 재정의 할 수 있습니다.

#일대일채팅 화면 view
@login_required
def singlechat(request, room_label, user, target_name):
    print("멍미?")
    room_inside = Oneroom.objects.get(pk=room_label)
    msg_list = room_inside.onemessages.all()
    nombre=user
    print(nombre)
    return render(request, 'chat_app/onechat.html', {
        #'room_name': room_inside, #admin, igidos;
        'nombre':nombre,
        'msg_list': msg_list,
        #'room_name':mark_safe(json.dumps(room_label)), #이렇게 안해주면 스크립트 코드 내에서 var roomName ={{ room_name }};이거 인식못함.
        'room_label':room_label,
        'target_name':target_name,
    })




