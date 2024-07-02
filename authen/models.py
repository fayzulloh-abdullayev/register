# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email manzil', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
