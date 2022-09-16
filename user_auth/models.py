from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    staff_types = [
        ('none', 'None'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    ]
    staff_type = models.CharField(max_length=50, choices=staff_types, default="none")
