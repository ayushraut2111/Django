from django.shortcuts import render,redirect
from . models import Room,Message
from django.http import HttpResponse,JsonResponse
def index(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    dic={'username':username,
         'room_details':room_details,
         'room':room}
    return render(request,'room.html',dic)

def chatroom(request):
    room_name=request.POST['room']
    username=request.POST['username']
    if Room.objects.filter(name=room_name).exists():
        return redirect("/"+room_name+'/?username='+username)
    else:
        Room.objects.create(name=room_name)
        Room.save()
        return redirect("/"+room_name+'/?username='+username)
    
def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    print(message,username,room_id)
    newmsg=Message.objects.create(value=message,user=username,room=room_id)
    newmsg.save()
    return HttpResponse("message saved succesffully")

def getmessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    # print(list(messages.values()))
    return JsonResponse({"messages":list(messages.values())})
