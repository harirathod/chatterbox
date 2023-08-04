from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators
import django.core.validators

# Create your models here.

class User(AbstractUser):
    """Class defining a user for the microblogs app."""
    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'}, 
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', 
        max_length=30, 
        unique=True, 
        validators=[
            django.contrib.auth.validators.UnicodeUsernameValidator(), 
            django.core.validators.RegexValidator(
                regex=r"^@[A-Za-z0-9]+$", 
                message="Username must consist of @ follows by alphanumericals.",
                ),
        ], 
        verbose_name='username')
    bio = models.CharField(
        default="No bio provided.",
        blank=True,
        unique=False,
        max_length=520,
        verbose_name="bio")
    first_name = models.CharField(
        blank=False, 
        unique=False,
        max_length=50, 
        verbose_name='first name')
    last_name = models.CharField(
        blank=False, 
        unique=False,
        max_length=50, 
        verbose_name='last name')
    email = models.EmailField(
        blank=False, 
        unique=True,
        max_length=520, 
        verbose_name='email address',)

