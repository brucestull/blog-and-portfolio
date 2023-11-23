from django.test import TestCase
from django.urls import reverse

from config.settings import THE_SITE_NAME

from accounts.models import CustomUser

from portfolio.models import (
    Project,
)


class TestProjectUpdateView(TestCase):
    """
    Test the `ProjectUpdateView` view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a user and a project.
        """
        cls.user1 = CustomUser.objects.create_user(
            username="testuser1",
            email="testuser1@email.app",
            password="testpassword1",
        )
        cls.user2 = CustomUser.objects.create_user(
            username="testuser2",
            email="testuser2@email.app",
            password="testpassword2",
        )
        cls.project = Project.objects.create(
            owner=cls.user1,
            title="Test Project",
            description="Test description",
            main_image="test.jpg",
        )

    def test_view_get_method_returns_200(self):
        """
        `ProjectUpdateView` `get()` method should return a 200 response.
        """
        self.client.login(username="testuser1", password="testpassword1")
        response = self.client.get(
            reverse(
                "portfolio:project-update",
                kwargs={"pk": self.project.pk},
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_view_has_correct_context_values(self):
        """
        `ProjectUpdateView` should have the correct context values.
        """
        self.client.login(username="testuser1", password="testpassword1")
        response = self.client.get(
            reverse(
                "portfolio:project-update",
                kwargs={"pk": self.project.pk},
            ),
        )
        self.assertEqual(response.context["page_title"], "Update Project")
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)
        self.assertEqual(response.context["project"], self.project)

    def test_view_accessible_by_name(self):
        """
        `ProjectUpdateView` should be accessible by name.
        """
        self.client.login(username="testuser1", password="testpassword1")
        response = self.client.get(
            reverse(
                "portfolio:project-update",
                kwargs={"pk": self.project.pk},
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_url(self):
        """
        `ProjectUpdateView` should be accessible by URL.
        """
        self.client.login(username="testuser1", password="testpassword1")
        response = self.client.get(f"/portfolio/projects/{self.project.pk}/update/")
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_only_by_owner(self):
        """
        `ProjectUpdateView` should only be accessible by the owner of the
        project.
        """
        self.client.login(username="testuser1", password="testpassword1")
        response = self.client.get(
            reverse(
                "portfolio:project-update",
                kwargs={"pk": self.project.pk},
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_view_inaccessible_by_non_owner(self):
        """
        `ProjectUpdateView` should be inaccessible by a user who did not
        create the project.
        """

        self.client.login(username="testuser2", password="testpassword2")
        response = self.client.get(
            reverse(
                "portfolio:project-update",
                kwargs={"pk": self.project.pk},
            ),
        )
        self.assertEqual(response.status_code, 403)
