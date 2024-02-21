# myproject/users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/')

    groups = models.ManyToManyField(Group, related_name='custom_groups')
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='custom_user_permissions')

    def __str__(self):
        return self.email
