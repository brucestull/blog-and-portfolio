from django.core.management.base import BaseCommand

from accounts.models import CustomUser


class Command(BaseCommand):
    help = "Create a sample superuser named `TestUser`"
    username = "TestUser"
    password = "1234test"
    email = "TestUser@email.app"
    first_name = "Test"
    last_name = "User"
    registration_accepted = True

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--test", type=str, help="Test argument", default="DefaultTestArg"
        )

    def handle(self, *args, **kwargs):
        test = kwargs.get("test", "DefaultTestArg")
        self.stdout.write(f"Test argument: {test}")
        if not CustomUser.objects.filter(username=self.username).exists():
            custom_user = CustomUser.objects.create_superuser(
                username=self.username,
                password=self.password,
                email=self.email,
                first_name=self.first_name,
                last_name=self.last_name,
                registration_accepted=self.registration_accepted,
            )
            self.stdout.write(f"Superuser created: {custom_user}")
        else:
            self.stdout.write(
                f"Superuser already exists with username: {self.username}"
            )
