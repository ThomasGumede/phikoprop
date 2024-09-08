import uuid
from django.db import models
from django.dispatch import receiver
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
from django.db.models.signals import pre_delete, post_save
from django.contrib.auth import get_user_model
from accounts.models import AbstractCreate, RelationShip
from accounts.utilities.choices import Gender
from accounts.utilities.validators import verify_rsa_phone
from rooms.utilities.file_handlers import handle_room_content_upload, handle_room_cover_upload

PHONE_VALIDATOR = verify_rsa_phone()

class StatusChoices(models.TextChoices):
    NOT_APPROVED = ("NOT APPROVED", "Not approved")
    PENDING = ("PENDING", "Pending")
    APPROVED = ("APPROVED", "Approved")

PROVINCES = [
    ("kzn", "KwaZulu-Natal"),
    ("mp", "Mpumalanga"),
    ("nw", "North-West"),
    ("fs", "Free-State"),
    ("wc", "Western Cape"),
    ("lp", "Limpopo"),
    ("gp", "Gauteng"),
    ("ec", "Eastern Cape"),
    ("nc", "Northern Cape"),
]

class Amenity(AbstractCreate):
    cover_image = models.ImageField(upload_to=handle_room_cover_upload)
    title = models.CharField(max_length=225, unique=True)
    room = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Amenity, self).save(*args, **kwargs)
    
class RoomType(AbstractCreate):
    cover_image = models.ImageField(upload_to=handle_room_cover_upload)
    title = models.CharField(help_text=_("Enter room name e.g Single Rooms"), max_length=250, unique=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True)
    description = HTMLField(help_text=_("Describe the room"))
    room_size = models.CharField(help_text=_("Enter room size in squere feet e.g 1200 sq.ft"), max_length=50)
    number_of_beds = models.IntegerField(help_text=_("Enter number of beds in room"), default=1)
    number_of_rooms = models.IntegerField(help_text=_("Enter number of rooms available for this room"), default=5)
    amenities = models.ManyToManyField(Amenity, related_name="rooms")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("Room Type")
        verbose_name_plural = _("Room Types")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(RoomType, self).save(*args, **kwargs)

class Room(AbstractCreate):
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.CASCADE)
    tenant = models.OneToOneField(get_user_model(), related_name="room", on_delete=models.CASCADE)
    occuppied_on = models.DateTimeField(null=True, blank=True)
    room_number = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.room_number

class RoomContent(AbstractCreate):
    room = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="room_contents")
    image = models.ImageField(upload_to=handle_room_content_upload)


class RoomApplication(AbstractCreate):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="applications")
    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="application")
    applicant_email = models.EmailField()
    applicant_phone = models.CharField(help_text=_("Enter your cellphone number"), max_length=15, validators=[PHONE_VALIDATOR], unique=True)
    applicant_first_name = models.CharField(help_text=_("Enter your name"), max_length=300)
    applicant_last_name = models.CharField(help_text=_("Enter your last name"), max_length=300)
    applicant_identity_number = models.CharField(unique=True, max_length=14)
    applicant_gender = models.CharField(help_text=_("Select relative's gender"), max_length=15, choices=Gender.choices, null=True, blank=True)

    relative_first_name = models.CharField(help_text=_("Enter your relative's name"), max_length=300)
    relative_last_name = models.CharField(help_text=_("Enter your relative's last name"), max_length=300)
    relationship = models.CharField(max_length=300, choices=RelationShip.choices, default=RelationShip.OTHER)
    relative_phone = models.CharField(help_text=_("Enter relative's cell phone number"), max_length=15,  validators=[PHONE_VALIDATOR])
    relative_email = models.EmailField(max_length=254)

    address_one = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    province = models.CharField(max_length=300, choices=PROVINCES)
    country = models.CharField(max_length=300, default="South Africa")
    zipcode = models.BigIntegerField()
    application_status = models.CharField(max_length=150, choices=StatusChoices.choices, default=StatusChoices.PENDING)

    class Meta:
        verbose_name = _("Room Application")
        verbose_name_plural = _("Room Applications")
        ordering = ["-created"]

    def __str__(self) -> str:
        return f"Application for {self.applicant} on room {self.room_type}"
