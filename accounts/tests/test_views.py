from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from accounts.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)


class CustomUserSignUpViewTest(TestCase):
    """
    Tests for `SignUpView`.
    """

    def test_view_url_exists(self):
        """
        URL "/accounts/signup/" should return status 200.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        """
        View name "signup" should return status 200.
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_form(self):
        """
        View should use form `CustomUserCreationForm`.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        # Test that the form is an instance of `CustomUserCreationForm`.
        self.assertIsInstance(
            response.context["form"],
            CustomUserCreationForm
        )
        # Alternative ways to test the form:
        # Test that the form's class is `CustomUserCreationForm`.
        self.assertEqual(
            response.context["form"].__class__, CustomUserCreationForm)
        # Test that the form's class name is the string
        # `CustomUserCreationForm`.
        self.assertEqual(
            response.context["form"].__class__.__name__,
            "CustomUserCreationForm"
        )

    def test_redirects_to_login_page_on_success(self):
        """
        User should be redirected to the login page on successful signup.
        """
        response = self.client.post(
            "/accounts/signup/",
            {
                "username": "DezziKitten",
                "password1": "MeowMeow42",
                "password2": "MeowMeow42",
                "first_name": "Dezzi",
            },
        )
        self.assertRedirects(response, "/accounts/login/")

    def test_uses_correct_template(self):
        """
        View should use "registration/signup.html" template.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_context_has_the_site_name(self):
        """

        View `context` should have a value "FlynntKnapp" for `the_site_name`.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "FlynntKnapp")


class CustomLoginViewTest(TestCase):
    """
    Tests for `CustomLoginView`.
    """

    def test_url_exists(self):
        """
        URL "/accounts/login/" should return status 200.
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        View name CUSTOM_LOGIN_VIEW_NAME should return status 200.
        """
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_context_has_the_site_name(self):
        """
        View `context` should have a value of "FlynntKnapp" for
        `the_site_name`.
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "FlynntKnapp")


class CustomUserUpdateViewTest(TestCase):
    """
    Tests for `CustomUserUpdateView`.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.test_kitten = CustomUser.objects.create_user(
            username="DezziKitten",
            password="MeowMeow42",
        )

    def test_model_is_custom_user(self):
        """
        View model should be `CustomUser`.
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["view"].model, CustomUser)

    def test_form_class_is_custom_user_change_form(self):
        """
        View form class should be `CustomUserChangeForm`.
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["view"].form_class,
            CustomUserChangeForm
        )

    def test_success_url_is_login(self):
        """
        View success URL should be "/accounts/login/".
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["view"].success_url,
            "/accounts/login/"
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertRedirects(
            response,
            "/accounts/login/" + "?next="
            f"/accounts/{self.test_kitten.pk}/edit/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_view_uses_correct_template(self):
        """
        View should use USER_UPDATE_VIEW_TEMPLATE.
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/update.html")

    def test_user_is_self_object(self):
        """
        User should only be able to edit their own account.
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.test_kitten)

    def test_view_returns_403_for_user_updating_another_user(self):
        """
        User should not be able to edit another user's account.
        """
        test_kitten_02 = CustomUser.objects.create_user(
            username="BunbunKitten",
            password="MeowMeow42",
        )
        self.client.force_login(test_kitten_02)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 403)

    def test_the_site_name_in_context(self):
        """
        View `context` should have a value of "FlynntKnapp" for
        "the_site_name".
        """
        self.client.force_login(self.test_kitten)
        response = self.client.get(
            reverse(
                "edit",
                kwargs={"pk": self.test_kitten.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["the_site_name"], "FlynntKnapp")


class CustomUserDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Create a test user and add it as an attribute of the `cls`.
        """
        cls.test_kitten_01 = CustomUser.objects.create_user(
            username="DezziKitten",
            password="MeowMeow42",
        )

    def test_url_redirects_non_authenticated_user(self):
        """
        URL should redirect for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.test_kitten_01.pk},
            )
        )
        self.assertRedirects(
            response,
            "/accounts/login/" + "?next="
            f"/accounts/{self.test_kitten_01.pk}/detail/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_view_uses_correct_template(self):
        """
        View should use "registration/detail.html".
        """
        self.client.force_login(self.test_kitten_01)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.test_kitten_01.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/customuser_detail.html")

    def test_user_is_self_object(self):
        """
        User should only be able to view their own account.
        """
        self.client.force_login(self.test_kitten_01)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.test_kitten_01.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.test_kitten_01)

    def test_view_returns_403_for_user_viewing_another_user(self):
        """
        User should not be able to view another user's account.
        """
        test_kitten_02 = CustomUser.objects.create_user(
            username="BunbunKitten",
            password="MeowMeow42",
        )
        self.client.force_login(test_kitten_02)
        response = self.client.get(
            reverse(
                "detail",
                kwargs={"pk": self.test_kitten_01.pk},
            )
        )
        self.assertEqual(response.status_code, 403)
