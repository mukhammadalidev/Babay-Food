from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, phone, password, **extra_fields):
        if not  phone:
            raise ValueError('Phone is required')
        self.phone = phone
        user = self.model(phone=self.phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(phone, password, **extra_fields)


import uuid

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message='Phone number must be entered in the format: +999999999')
    phone = models.CharField( validators=[phone_regex], max_length=17,
                             unique=True)  # validators should be a list
    is_partner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()