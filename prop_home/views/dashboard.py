from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

from prop_home.utilities.decorators import user_not_superuser_or_staff
from rooms.models import Room

USER = get_user_model()

@login_required
def get_dashboard(request, username):
    return render(request, "home/dashboard/get-dashboard.html")

@login_required
@user_not_superuser_or_staff
def all_accounts(request):
    template = "dashboard/accounts/users.html"
    query = request.GET.get("q", None)
    users = USER.objects.all()
    if query:
        users = USER.objects.filter(
            Q(username__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query) 
            | Q(address_one__icontains = query)
        )
        
    return render(request, "home/dashboard/accounts/all-accounts.html", {"accounts": users, "query": query})

@login_required
@user_not_superuser_or_staff
def manage_rooms(request):
    rooms = Room.objects.all()
    return render(request, "home/dashboard/rooms/manage-rooms.html", {"rooms": rooms})

@login_required
@user_not_superuser_or_staff
def manage_room(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    return render(request, "home/dashboard/rooms/manage-room.html", {"room": room})

@login_required
@user_not_superuser_or_staff
def add_room(request):
    
    return render(request, "home/dashboard/rooms/add-room.html", {"form": "form"})

@login_required
@user_not_superuser_or_staff
def update_room(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    return render(request, "home/dashboard/rooms/update-room.html", {"room": room})

@login_required
@user_not_superuser_or_staff
def delete_room(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    return render(request, "home/dashboard/rooms/delete-room.html", {"room": room})




