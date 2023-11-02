
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm


# room = [
#     {'id': 1, 'name': 'lets learn Python'},
#     {'id': 2, 'name': 'lets learn Django'},
#     {'id': 3, 'name': 'lets learn Flask'},
#     {'id': 4, 'name': 'lets learn SQL'},
# ]


def home(request):
    rooms = Room.objects.all() 

    topic = Topic.objects.all()



    context = {'rooms': rooms,
                'topics': topic}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # ensure variable is set to none
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context) 

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


# using pk because we need to know which room we are updating
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')   
    context = {'form': form}

    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})