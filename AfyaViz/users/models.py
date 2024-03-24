from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    affiliation = models.CharField(max_length=255, blank=True)

    # Add related_name attributes to resolve the clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_users'  # Use a custom related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set'  # Use a custom related_name
    )
