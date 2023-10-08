from django.core.management.base import CommandError, BaseCommand
from faker import Faker
from microblogs.models import User

# This class must be named Command to be recognised by Django. We cannot give it a custom name.

class Command(BaseCommand):
    """This class defines what happens when the 'seed' command is called.
    
    It creates 100 fake entries in the database."""
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        """This code is run when 'python3 manage.py seed' is called."""
        for _ in range(100):
            # If we just used 'create', this wouldn't hash the password. Thus, we need to user "create_user()"
            user = User.objects.create_user(
                username = self.faker.unique.user_name(),
                password = self.faker.password(),
                bio = self.faker.text(),
                first_name = self.faker.first_name(),
                last_name = self.faker.last_name(),
                email = self.faker.email(),
            )
            # user.save() is not needed. 
        print("Created fake users.")

# Currently on the new branch