from django.test import TestCase

from accounts.models import CustomUser

from portfolio.models import Project, Technology
from portfolio.admin import ProjectAdmin, TechnologyAdmin


class TestTechnologyAdmin(TestCase):
    """
    Test the `TechnologyAdmin` class.
    """

    def test_list_display(self):
        """
        `list_display` should contain the following fields:
        - `name`
        - `description`
        - `created_at`
        """
        technology_admin = TechnologyAdmin(Technology, None)
        self.assertIn("name", technology_admin.list_display)
        self.assertIn("description", technology_admin.list_display)
        self.assertIn("created_at", technology_admin.list_display)

    def test_get_fieldsets_is_list_of_tuples(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list
        of tuples.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        self.assertIsInstance(fieldsets, list)
        self.assertIsInstance(fieldsets[0], tuple)

    def test_get_fieldsets_has_name_in_first_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list
        of tuples that includes `name`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("name", fieldsets_as_list[0][1]["fields"][0])

    def test_get_fieldsets_has_description_in_second_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list
        of tuples that includes `description`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("description", fieldsets_as_list[0][1]["fields"][1])

    def test_get_fieldsets_has_created_at_in_third_element(self):
        """
        `TechnologyAdmin` `get_fieldsets()` method should return a list
        of tuples that includes `created_at`.
        """
        technology_admin = TechnologyAdmin(Technology, None)
        fieldsets = technology_admin.get_fieldsets(request=None, obj=None)
        fieldsets_as_list = list(fieldsets)
        self.assertIn("created_at", fieldsets_as_list[0][1]["fields"][2])

    def test_readonly_fields(self):
        """
        `readonly_fields` should contain the following fields:
        - `created_at`
        - `updated_at`
        """
        technology_admin = TechnologyAdmin(Technology, None)
        self.assertIn("created_at", technology_admin.readonly_fields)
        self.assertIn("updated_at", technology_admin.readonly_fields)


class TestProjectAdmin(TestCase):
    """
    Test the `ProjectAdmin` class.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a `user` and `project` for testing.
        """
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@email.app",
            password="testpassword",
        )
        cls.project = Project.objects.create(
            owner=cls.user,
            title="Test Project",
            description="Test description",
            main_image="test.jpg",
        )

    def test_list_display(self):
        """
        `list_display` should contain the following fields:
        - `title`
        - `truncated_description`
        - `display_technologies`
        - `main_image`
        - `created_at`
        """
        project_admin = ProjectAdmin(Project, None)
        self.assertIn("title", project_admin.list_display)
        self.assertIn("truncated_description", project_admin.list_display)
        self.assertIn("display_technologies", project_admin.list_display)
        self.assertIn("main_image", project_admin.list_display)
        self.assertIn("created_at", project_admin.list_display)

    def test_readonly_fields(self):
        """
        `readonly_fields` should contain the following fields:
        - `created_at`
        - `updated_at`
        """
        project_admin = ProjectAdmin(Project, None)
        self.assertIn("created_at", project_admin.readonly_fields)
        self.assertIn("updated_at", project_admin.readonly_fields)

    def test_truncated_description_method_returns_description(self):
        """
        `ProjectAdmin` `truncated_description()` method should return the
        `description` when it is less than or equal to 30 characters.
        """
        project_admin = ProjectAdmin(Project, None)
        project = Project.objects.create(
            owner=self.user,
            title="Test Project",
            description="Test description",
            main_image="test.jpg",
        )
        self.assertEqual(
            project_admin.truncated_description(project),
            project.description,
        )

    def test_truncated_description_method_returns_truncated_description(
        self,
    ):
        """
        `ProjectAdmin` `truncated_description()` method should return
        the truncated `description` when it is greater than 30 characters.
        """
        test_description_more_than_30_characters = (
            "This is a description with more than 30 characters."
        )
        project_admin = ProjectAdmin(Project, None)
        project = Project.objects.create(
            owner=self.user,
            title="Test Project",
            description=test_description_more_than_30_characters,
            main_image="test.jpg",
        )
        truncated_description = test_description_more_than_30_characters[:30]
        self.assertEqual(
            project_admin.truncated_description(project),
            truncated_description,
        )
