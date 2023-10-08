from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    """This class defines what happens when the 'show' command is called.
    
    It lists all users in the database, in the format 'username, first_name, last_name, email'"""
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        """This code is run when 'python3 manage.py show' is called."""
        users = User.objects.all()
        if (users):
            for user in User.objects.all():
                print(f'User Details: {user.username}, {user.first_name} {user.last_name}, {user.email}')
        else:
            print('There are no users in the database.')
        
