from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

# This class must be named Command to be recognised by Django. We cannot give it a custom name.

class Command(BaseCommand):
    """This class defines what happens when the 'unseed' command is called. 
    
    It deletes all entries from the database."""
    def __init__(self):
        super().__init__()
        
    def handle(self, *args, **options):
        """This code is run when 'python3 manage.py unseed' is called."""
        for user in User.objects.all():
            user.delete()
        print("Deleted all users from the database.")
    
# Currently on the new branch