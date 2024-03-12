import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from accounts.models import CustomUser

USERNAME = "FlipJohnson"
PASSWORD = "1234test"
EMAIL = "FlipJohnson@email.app"


def create_a_super_user(username, password, email):
    if not CustomUser.objects.filter(username=username).exists():
        custom_user = CustomUser.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )
        print(f"Superuser created: {custom_user}")
    else:
        print(f"Superuser already exists with username: {username}")


if __name__ == "__main__":
    create_a_super_user(USERNAME, PASSWORD, EMAIL)
