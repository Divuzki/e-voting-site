from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        # username = self.normalize_username(username)
        user = CustomUser(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Admin"), (2, "Voter"))
    username = models.CharField(max_length=225, unique=True)  # Removed username, using email instead
    mat_num = models.CharField(max_length=50, unique=True)
    user_type = models.CharField(default=2, choices=USER_TYPE, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + " " + self.first_name
