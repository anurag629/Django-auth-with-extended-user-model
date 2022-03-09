from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager

typee = (
    ('paitent' , 'Paitent'),
    ('doctor' , 'Doctor'),
)

class User(AbstractUser):
    types_user = models.CharField(
        max_length = 10,
        choices = typee,
        default = 'doctor'
        )
    email = models.EmailField(unique=True)
    pic = models.ImageField(upload_to='media/profile')
    address_line1 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(null = True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager
