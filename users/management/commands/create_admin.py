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

        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            raise CommandError(f"Username `{username}` already taken.")

        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(username=username, email=email, password=password)

        return f"Admin `{username}` successfully created!"
