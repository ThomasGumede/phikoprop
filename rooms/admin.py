from django.contrib import admin
from rooms.models import *

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomApplication)
class RoomApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomContent)
class RoomContentAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass