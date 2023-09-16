from django.test import TestCase

from accounts.models import CustomUser
from accounts.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)
from accounts.admin import CustomUserAdmin


TEST_USERNAME_ONE = 'CustomUser01'
TEST_PASSWORD_ONE = 'TEST_PASSWORD_ONE'
TEST_FIRST_NAME_ONE = 'One'

TEST_USERNAME_TWO = 'CustomUser02'
TEST_PASSWORD_TWO = 'TEST_PASSWORD_TWO'
TEST_FIRST_NAME_TWO = 'Two'


class TestCustomUserAdmin(TestCase):
    """
    Tests for `CustomUserAdmin`.
    """

    def test_add_form_is_correct(self):
        """
        `CustomUserAdmin` `add_form` should be `CustomUserCreationForm`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(
            custom_user_admin.add_form.__name__,
            "CustomUserCreationForm"
        )
        self.assertEqual(
            custom_user_admin.add_form,
            CustomUserCreationForm
        )

    def test_form_is_correct(self):
        """
        `CustomUserAdmin` `form` should be `CustomUserChangeForm`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(
            custom_user_admin.form.__name__,
            "CustomUserChangeForm"
        )
        self.assertEqual(
            custom_user_admin.form,
            CustomUserChangeForm
        )

    def test_model_is_correct(self):
        """
        `CustomUserAdmin` `model` should be `CustomUser`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(custom_user_admin.model, CustomUser)

    def test_list_display_is_correct(self):
        """
        `CustomUserAdmin` `list_display` should be a tuple containing
        `username` and `registration_accepted`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        self.assertEqual(
            custom_user_admin.list_display,
            (
                "username",
                "email",
                "registration_accepted"
            )
        )

    def test_get_fieldsets_returns_list_of_tuples(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of
        tuples.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        self.assertIsInstance(fieldsets, list)
        self.assertIsInstance(fieldsets[0], tuple)

    def test_get_fieldsets_has_moderator_permissions_in_second_element(self):
        """
        `CustomUserAdmin` `get_fieldsets()` method should return a list of
        tuples that includes `Moderator Permissions`.
        """
        custom_user_admin = CustomUserAdmin(CustomUser, None)
        fieldsets = custom_user_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("Moderator Permissions", fieldsets_as_list[1])
