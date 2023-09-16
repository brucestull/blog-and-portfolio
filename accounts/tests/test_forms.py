from django.test import TestCase

from accounts.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)

from accounts.models import CustomUser


class TestCustomUserCreationForm(TestCase):
    """
    Tests for `CustomUserCreationForm`.
    """

    def test_meta_model(self):
        """
        Test `CustomUserCreationForm.Meta.model`.
        """
        self.assertEqual(
            CustomUserCreationForm.Meta.model,
            CustomUser,
        )

    def test_meta_fields(self):
        """
        Test `CustomUserCreationForm.Meta.fields`.
        """
        self.assertEqual(
            CustomUserCreationForm.Meta.fields,
            (
                "username",
                "email",
            ),
        )


class TestCustomUserChangeForm(TestCase):
    """
    Tests for `CustomUserChangeForm`.
    """

    def test_meta_model(self):
        """
        Test `CustomUserChangeForm.Meta.model`.
        """
        self.assertEqual(
            CustomUserChangeForm.Meta.model,
            CustomUser,
        )

    def test_meta_fields(self):
        """
        Test `CustomUserChangeForm.Meta.fields`.
        """
        self.assertEqual(
            CustomUserChangeForm.Meta.fields,
            (
                "username",
                "email",
                "first_name",
                "last_name",
            ),
        )
