from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    # Establishing a many-to-many relationship with Role
    roles = models.ManyToManyField(Role, related_name='users')

    def __str__(self):
        return self.username

# Override the groups and user_permissions fields to avoid clashes
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_users'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_users'
