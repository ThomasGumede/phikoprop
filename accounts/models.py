import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from accounts.utilities.choices import TITLE_CHOICES, Gender
from accounts.utilities.validators import validate_sa_id_number, verify_rsa_phone
from accounts.utilities.file_handlers import handle_profile_upload

PHONE_VALIDATOR = verify_rsa_phone()

class AbstractCreate(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class RelationShip(models.TextChoices):
    OTHER = ("OTHER", "Other")
    MOTHER = ("MOTHER", "Mother")
    FATHER = ("FATHER", "Father")
    STEPMOTHER = ("STEPMOTHER", "Step-mother")
    STEPFATHER = ("STEPFATHER", "Step-father")
    GRANDMOTHER = ("GRANDMOTHER", "Grandmother")
    GRANDFATHER = ("GRANDFATHER", "Grandfather")
    BROTHER = ("BROTHER", "Brother")
    SISTER = ("SISTER", "Sister")
    COUSIN = ("COUSIN", "Cousin")
    AUNT = ("AUNT", "Aunt")
    UNCLE = ("UNCLE", "Uncle")

class Account(AbstractUser):
    profile_image = models.ImageField(help_text=_("Upload profile image"), upload_to=handle_profile_upload, null=True, blank=True)
    title = models.CharField(max_length=30, choices=TITLE_CHOICES, null=True, blank=True)
    gender = models.CharField(help_text=_("Select relative's gender"), max_length=15, choices=Gender.choices, null=True, blank=True)
    maiden_name = models.CharField(help_text=_("Enter your maiden name"), max_length=300, blank=True, null=True)
    phone = models.CharField(help_text=_("Enter your cellphone number"), max_length=15, validators=[PHONE_VALIDATOR], unique=True, null=True, blank=True)
    biography = models.TextField(blank=True)
    identity_number = models.CharField(unique=True, max_length=15, null=True, blank=True)
    is_technical = models.BooleanField(default=False)
    is_email_activated = models.BooleanField(default=False)
    address_one = models.CharField(max_length=300, blank=True, null=True)
    address_two = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    province = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=300, default="South Africa")
    zipcode = models.BigIntegerField(blank=True, null=True)
    address_id = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["-created"]

    def __str__(self):
        return self.get_full_name()
    
    def get_address(self):
        return f"{self.address_one}, {self.city}"

class RelativeModel(AbstractCreate):
    title = models.CharField(max_length=30, choices=TITLE_CHOICES)
    full_name = models.CharField(help_text=_("Enter your relative's name"), max_length=300)
    maiden_name = models.CharField(help_text=_("Enter your relative's maiden name"), max_length=300, blank=True, null=True)
    surname = models.CharField(help_text=_("Enter your relative's surname"), max_length=300)
    relationship = models.CharField(max_length=300, choices=RelationShip.choices, default=RelationShip.OTHER)
    phone = models.CharField(help_text=_("Enter relative's cell phone number"), max_length=15,  validators=[PHONE_VALIDATOR], null=True, blank=True)
    email = models.EmailField(max_length=254)
    relative = models.ForeignKey(Account, related_name="relatives", on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Relative'
        verbose_name_plural = 'Relatives'
        unique_together = ['title', 'full_name', 'maiden_name', 'surname', 'relative', 'relationship', 'phone', 'email']

    # def get_absolute_url(self):
    #     return reverse("accounts:relative", kwargs={"id": self.id})

    def get_full_names(self):
        if self.maiden_name != None:
            return f"{self.title} {self.full_name} {self.surname} {self.maiden_name}"
        else:
            return f"{self.title} {self.full_name} {self.surname}"
        
    def get_info(self):
        return f"{self.relative.get_full_name()}'s {self.relationship}"
    
    def __str__(self):
        return self.full_name
 

