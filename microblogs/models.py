from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators

# Create your models here.

class User(AbstractUser):
    """Class defining a user for the microblogs app."""
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    bio = models.TextField(default="No bio provided.")
