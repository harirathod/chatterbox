"""Configuration of the admin in the microblogs app."""

from django.contrib import admin
from .models import User    # .models is used to show we are referring to the current directory. models doesn't work.
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """Class defining an admin user, in the microblogs app."""
    list_display = [
        'username', 'first_name', 'is_active', 'date_joined', 'email',
    ]