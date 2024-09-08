from django.db import models

TITLE_CHOICES = (
    ("Mr", "Mr"),
    ("Mrs", "Mrs"),
    ("Ms", "Ms"),
    ("Dr", "Dr"),
    ("Prof", "Prof.")
)



class StatusChoices(models.TextChoices):
    NOT_APPROVED = ("NOT APPROVED", "Not approved")
    PENDING = ("PENDING", "Pending")
    APPROVED = ("APPROVED", "Approved")
    COMPLETED = ("Completed", "Completed")
    BLOCKED = ("Blocked", "Blocked")

class IdentityNumberChoices(models.TextChoices):
    ID_NUMBER = ("ID_NUMBER", "ID number")
    PASSPORT = ("PASSPORT", "Passport")

class Gender(models.TextChoices):
    MALE = ("MALE", "Male")
    FEMALE = ("FEMALE", "Female")
    OTHER = ("OTHER", "Other")


