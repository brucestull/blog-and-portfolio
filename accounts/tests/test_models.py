from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import CustomUser


class CustomUserModelTest(TestCase):
    """
    Tests for `CustomUser` model.
    """

    def test_registration_accepted_is_boolean_field(self):
        """
        `registration_accepted` field should be a `BooleanField`.
        """
        custom_user_field_type = CustomUser._meta.get_field(
            "registration_accepted").get_internal_type()
        self.assertEqual(custom_user_field_type, "BooleanField")

    def test_registration_accepted_verbose_name(self):
        """
        `registration_accepted` field should have verbose name of
        'Registration Accepted'.
        """
        custom_user_verbose_name = CustomUser._meta.get_field(
            "registration_accepted").verbose_name
        self.assertEqual(custom_user_verbose_name, "Registration Accepted")

    def test_registration_accepted_help_text(self):
        """
        `registration_accepted` field should have help text of
        'Designates whether user's registration has been accepted by an
        admin.'.
        """
        custom_user_help_text = CustomUser._meta.get_field(
            "registration_accepted").help_text
        self.assertEqual(
            custom_user_help_text,
            "Designates whether user's registration has been accepted "
            "by an admin."
        )

    def test_registration_accepted_default_false(self):
        """
        `registration_accepted` field should default to False.
        """
        custom_user_default = CustomUser._meta.get_field(
            "registration_accepted").default
        self.assertFalse(custom_user_default)

    def test_dunder_string_method(self):
        """
        `CustomUser` model `__str__` method should return `username`.
        """
        self.custom_user_01 = get_user_model().objects.create_user(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        self.assertEqual(str(self.custom_user_01), "DezziKitten")
