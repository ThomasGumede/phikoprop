from django.urls import path

from rooms.views.rooms import get_rooms, room_details, room_application, create_room, manage_rooms

app_name = "rooms"
urlpatterns = [
    path("rooms", get_rooms, name="get-rooms"),
    path("rooms/room-details/<slug:room_slug>", room_details, name="room-details"),
    path("dashboard/rooms/create-room", create_room, name="create-room"),
    path("dashboard/rooms/manage", manage_rooms, name="manage-rooms"),
    path("rooms/room-application/<slug:room_id>", room_application, name="room-application"),
]

