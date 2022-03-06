from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    pic = models.ImageField(upload_to='profile')
    address_line1 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    objects = UserManager

    USERNAME_FIELD = 'email'