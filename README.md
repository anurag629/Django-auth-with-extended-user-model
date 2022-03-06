# Django-auth-with-extended-user-model 

## 1. Create project and app :
* create project:

        django-admin startproject core
* create app inside the project main directory:

        python manage.py startapp accounts

## 2. Add app to settings.py file :
    INSTALLED_APPS = [
        ....,
        'accounts',
        ....,
    ]

## 3. Create models in models.py file :
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


## 4. Create file manager.py file inside accounts app and paste the following code :

    from django.contrib.auth.base_user import BaseUserManager

    class UserManager(BaseUserManager):
        use_in_migrations = True

        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('Email is require')
            email = self.normalize_email(email)
            user = self.model(email = email,  **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email,password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Super User must have is_staff true')

            return self.create_user(email, password, **extra_fields)
