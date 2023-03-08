from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create a new admin"

    def add_arguments(self, parser):
        parser.add_argument("--username", help="Define an username for admin.")
        parser.add_argument("--email", help="Define an email for admin.")
        parser.add_argument("--password", help="Define a password for admin.")

    def handle(self, *args, **kwargs):
        username = kwargs["username"] if kwargs["username"] else "admin"
        email = kwargs["email"] if kwargs["email"] else "admin@example.com"
        password = kwargs["password"] if kwargs["password"] else "admin1234"

        try:
            User.objects.get(username=username)
            raise CommandError(f"Username `{username}` already taken.")
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            raise CommandError(f"Email `{email}` already taken.")
        except User.DoesNotExist:
            pass

        User.objects.create_superuser(username=username, email=email, password=password)

        return f"Admin `{username}` successfully created!"
