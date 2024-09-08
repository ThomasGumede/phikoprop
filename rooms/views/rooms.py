from django.shortcuts import redirect, render
from rooms.forms import ApplicationForm, RoomTypeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rooms.models import RoomType

# Create your views here.
def get_rooms(request):
    return render(request, 'rooms/rooms.html')

@login_required
def manage_rooms(request):
    rooms = RoomType.objects.all()
    return render(request, 'rooms/manage/rooms.html', {"rooms": rooms})

def room_details(request, room_slug):
    return render(request, 'rooms/room.html')

@login_required
def create_room(request):
    if request.method == "POST":
        form = RoomTypeForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form.is_multipart():
            form.save()
            messages.success(request, "Room Added successfully")
            return redirect("prop_home:prop-home")
        else:
            messages.error(request, "Error tyring to add room")
            return render(request, 'rooms/manage/create-room.html', {"form": form})
    form = RoomTypeForm()
    return render(request, 'rooms/manage/create-room.html', {"form": form})

@login_required
def room_application(request, room_id):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            messages.success(request, "Room application successfully saved")
            return redirect("rooms:room-application-success")
        else:
            return render(request, 'rooms/room-application.html', {"form": form})
        
    form = ApplicationForm()
    return render(request, 'rooms/room-application.html', {"form": form})

@login_required
def room_application_success(request):
    return render(request, "rooms/success.html")