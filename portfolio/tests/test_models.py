from django.test import TestCase
from django.db import models as d_db_models

from accounts.models import CustomUser
from portfolio.models import (
    TimestampMixin,
    Technology,
    Project,
    ProjectImage,
)


class TimestampMixinTest(TestCase):
    """
    Tests for `TimestampMixin` model.
    """

    def test_created_at_verbose_name(self):
        """
        `TimestampMixin` model `created_at` field `verbose_name` should be
        "Created At".
        """
        created_at_verbose_name = TimestampMixin._meta.get_field(
            "created_at"
        ).verbose_name
        self.assertEqual(created_at_verbose_name, "Created At")

    def test_created_at_auto_now_add_true(self):
        """
        `TimestampMixin` model `created_at` field `auto_now_add` should be
        `True`.
        """
        auto_now_add = TimestampMixin._meta.get_field("created_at").auto_now_add
        self.assertTrue(auto_now_add)

    def test_updated_at_verbose_name(self):
        """
        `TimestampMixin` model `updated_at` field `verbose_name` should be
        "Updated At".
        """
        field_label = TimestampMixin._meta.get_field("updated_at").verbose_name
        self.assertEqual(field_label, "Updated At")

    def test_updated_at_auto_now_true(self):
        """
        `TimestampMixin` model `updated_at` field `auto_now` should be `True`.
        """
        auto_now = TimestampMixin._meta.get_field("updated_at").auto_now
        self.assertTrue(auto_now)

    def test_class_meta_abstract_true(self):
        """
        `TimestampMixin` model `Meta` class `abstract` should be `True`.
        """
        abstract = TimestampMixin._meta.abstract
        self.assertTrue(abstract)


class TechnologyTest(TestCase):
    """
    Tests for `Technology` model.
    """

    def test_name_verbose_name(self):
        """
        `Technology` model `name` field `verbose_name` should be
        "Technology Name".
        """
        name_verbose_name = Technology._meta.get_field("name").verbose_name
        self.assertEqual(name_verbose_name, "Technology Name")

    def test_name_help_text(self):
        """
        `Technology` model `name` field help text should be
        "Enter the name of the technology.".
        """
        name_help_text = Technology._meta.get_field("name").help_text
        self.assertEqual(name_help_text, "Enter the name of the technology.")

    def test_name_max_length(self):
        """
        `Technology` model `name` field max length should be 30.
        """
        name_max_length = Technology._meta.get_field("name").max_length
        self.assertEqual(name_max_length, 30)

    def test_description_label(self):
        """
        `Technology` model `description` field label should be `description`.
        """
        description_verbose_name = Technology._meta.get_field(
            "description"
        ).verbose_name
        self.assertEqual(description_verbose_name, "Technology Description")

    def test_description_help_text(self):
        """
        `Technology` model `description` field help text should be
        `Enter a description of the technology.`.
        """
        description_help_text = Technology._meta.get_field("description").help_text
        self.assertEqual(
            description_help_text,
            "Enter a description of the technology.",
        )

    def test_description_blank_true(self):
        """
        `Technology` model `description` field `blank` should be `True`.
        """
        description_blank = Technology._meta.get_field("description").blank
        self.assertTrue(description_blank)

    def test_description_null_true(self):
        """
        `Technology` model `description` field `null` should be `True`.
        """
        description_null = Technology._meta.get_field("description").null
        self.assertTrue(description_null)

    def test_dunder_string_method(self):
        """
        `Technology` model `__str__` method should return `name`.
        """
        technology = Technology.objects.create(
            name="Test Technology",
            description="Test Technology Description",
        )
        self.assertEqual(technology.__str__(), "Test Technology")

    def test_meta_verbose_name_plural(self):
        """
        `Technology` model `Meta` class `verbose_name_plural` should be
        `technologies`.
        """
        meta_verbose_name_plural = Technology._meta.verbose_name_plural
        self.assertEqual(meta_verbose_name_plural, "Technologies")


class ProjectTest(TestCase):
    """
    Tests for `Project` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create test date.
        """
        cls.a_test_kitten = CustomUser.objects.create(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        cls.technology_01 = Technology.objects.create(
            name="Django",
            description="Django Description",
        )
        cls.technology_02 = Technology.objects.create(
            name="Python",
            description="Python Description",
        )
        cls.technology_03 = Technology.objects.create(
            name="JavaScript",
            description="JavaScript Description",
        )
        cls.technology_04 = Technology.objects.create(
            name="HTML",
            description="HTML Description",
        )
        cls.project_01 = Project.objects.create(
            owner=cls.a_test_kitten,
            title="DezziKitten's Test Project",
            description="Test Project Description",
        )
        cls.project_01.technology.set([cls.technology_01])
        cls.project_02 = Project.objects.create(
            owner=cls.a_test_kitten,
            title="DezziKitten's Second Test Project",
            description="Second Test Project Description",
        )
        cls.project_02.technology.set([cls.technology_01, cls.technology_02])
        cls.project_04 = Project.objects.create(
            owner=cls.a_test_kitten,
            title="DezziKitten's Fourth Test Project",
            description="Fourth Test Project Description",
        )
        cls.project_04.technology.set(
            [
                cls.technology_01,
                cls.technology_02,
                cls.technology_03,
                cls.technology_04,
            ]
        )

    def test_owner_verbose_name(self):
        """
        `Project` model `owner` field `verbose_name` should be "Owner".
        """
        owner_verbose_name = Project._meta.get_field("owner").verbose_name
        self.assertEqual(owner_verbose_name, "Owner")

    def test_owner_help_text(self):
        """
        `Project` model `owner` field help text should be
        "Owner of this project.".
        """
        owner_help_text = Project._meta.get_field("owner").help_text
        self.assertEqual(owner_help_text, "Owner of this project.")

    def test_owner_on_delete_cascade(self):
        """
        `Project` model `owner` field `on_delete` should be `models.CASCADE`.
        """
        owner_on_delete = Project._meta.get_field("owner")
        self.assertEqual(owner_on_delete.remote_field.on_delete, d_db_models.CASCADE)

    def test_owner_related_name(self):
        """
        `Project` model `owner` field related name should be `projects`.
        """
        owner_related_name = Project._meta.get_field("owner").related_query_name()
        self.assertEqual(owner_related_name, "projects")

    def test_title_verbose_name(self):
        """
        `Project` model `title` field `verbose_name` should be "Project Title".
        """
        title_verbose_name = Project._meta.get_field("title").verbose_name
        self.assertEqual(title_verbose_name, "Project Title")

    def test_title_help_text(self):
        """
        `Project` model `title` field help text should be
        "Enter the title of the project.".
        """
        title_help_text = Project._meta.get_field("title").help_text
        self.assertEqual(title_help_text, "Enter the title of the project.")

    def test_title_max_length(self):
        """
        `Project` model `title` field max length should be 100.
        """
        title_max_length = Project._meta.get_field("title").max_length
        self.assertEqual(title_max_length, 100)

    def test_description_verbose_name(self):
        """
        `Project` model `description` field label should be `description`.
        """
        description_verbose_name = Project._meta.get_field("description").verbose_name
        self.assertEqual(description_verbose_name, "Project Description")

    def test_description_help_text(self):
        """
        `Project` model `description` field help text should be
        "Enter a description of the project.".
        """
        description_help_text = Project._meta.get_field("description").help_text
        self.assertEqual(
            description_help_text,
            "Enter a description of the project.",
        )

    def test_description_blank_true(self):
        """
        `Project` model `description` field `blank` should be `True`.
        """
        description_blank = Project._meta.get_field("description").blank
        self.assertTrue(description_blank)

    def test_description_null_true(self):
        """
        `Project` model `description` field `null` should be `True`.
        """
        description_null = Project._meta.get_field("description").null
        self.assertTrue(description_null)

    def test_repository_url_verbose_name(self):
        """
        `Project` model `repository_url` field label should be
        `repository_url`.
        """
        repository_url_verbose_name = Project._meta.get_field(
            "repository_url"
        ).verbose_name
        self.assertEqual(repository_url_verbose_name, "Repository URL")

    def test_repository_url_help_text(self):
        """
        `Project` model `repository_url` field help text should be
        "Enter the URL of the project's repository.".
        """
        repository_url_help_text = Project._meta.get_field("repository_url").help_text
        self.assertEqual(
            repository_url_help_text,
            "Enter the URL of the project's repository.",
        )

    def test_repository_url_blank_true(self):
        """
        `Project` model `repository_url` field `blank` should be `True`.
        """
        repository_url_blank = Project._meta.get_field("repository_url").blank
        self.assertTrue(repository_url_blank)

    def test_repository_url_null_true(self):
        """
        `Project` model `repository_url` field `null` should be `True`.
        """
        repository_url_null = Project._meta.get_field("repository_url").null
        self.assertTrue(repository_url_null)

    def test_technology_verbose_name(self):
        """
        `Project` model `technology` field label should be `technology`.
        """
        technology_verbose_name = Project._meta.get_field("technology").verbose_name
        self.assertEqual(technology_verbose_name, "Technologies")

    def test_technology_help_text(self):
        """
        `Project` model `technology` field help text should be
        "Enter the technology used in the project.".
        """
        technology_help_text = Project._meta.get_field("technology").help_text
        self.assertEqual(
            technology_help_text,
            "Select a technology for this project.",
        )

    def test_main_image_field(self):
        """
        `Project` model `main_image` field should have the following
        attributes:

        - `verbose_name` should be "Main Image"
        - `help_text` should be "Add an image of the project."
        - `upload_to` should be "portfolio/"
        - `blank` should be "True"
        - `null` should be "True"
        """
        main_image_verbose_name = Project._meta.get_field("main_image").verbose_name
        self.assertEqual(main_image_verbose_name, "Main Image")
        main_image_help_text = Project._meta.get_field("main_image").help_text
        self.assertEqual(main_image_help_text, "Add an image of the project.")
        main_image_upload_to = Project._meta.get_field("main_image").upload_to
        self.assertEqual(main_image_upload_to, "portfolio/")
        main_image_blank = Project._meta.get_field("main_image").blank
        self.assertTrue(main_image_blank)
        main_image_null = Project._meta.get_field("main_image").null
        self.assertTrue(main_image_null)

    # TODO: Fix this test.
    # def test_image_path(self):
    #     """
    #     `Project` model `image` field path should be `/img`.
    #     """
    #     path = self.project._meta.get_field(TEST_PROJECT_IMAGE_LABEL).path
    #     self.assertEqual(path, PROJECT_IMAGE_PATH)

    def test_dunder_string_method(self):
        """
        `Project` model `__str__` method should return `title`.
        """
        self.assertEqual(
            self.project_01.__str__(),
            "DezziKitten's Test Project",
        )

    def test_get_absolute_url_method(self):
        """
        `Project` model `get_absolute_url` method should return
        `/portfolio/<project_id>/`.
        """
        self.assertEqual(
            self.project_01.get_absolute_url(),
            f"/portfolio/projects/{self.project_01.id}/",
        )

    def test_display_technologies_method_with_one_technology(self):
        """
        `Project` model `display_technologies` method should return
        one technology.
        """
        self.assertEqual(
            self.project_01.display_technologies(),
            self.technology_01.name,
        )

    def test_display_technologies_method_with_two_technologies(self):
        """
        `Project` model `display_technologies` method should return
        two technologies.
        """
        self.assertEqual(
            self.project_02.display_technologies(),
            f"{self.technology_01.name}, {self.technology_02.name}",
        )

    def test_display_technologies_method_with_four_technologies(self):
        """
        `Project` model `display_technologies` method should return the
        first three technologies if there are more than three.
        """
        self.assertEqual(
            self.project_04.display_technologies(),
            f"{self.technology_01.name}, {self.technology_02.name}, "
            f"{self.technology_03.name}",
        )


class ProjectImageModelTest(TestCase):
    """
    Tests for `ProjectImage` model.
    """

    def test_project_field(self):
        """
        `ProjectImage` model `project` field should have the following
        attributes:

        - `verbose_name` should be "Project"
        - `help_text` should be "Project to which this image belongs."
        - `on_delete` should be `models.CASCADE`
        - `related_name` should be `images`
        """
        project_verbose_name = ProjectImage._meta.get_field("project").verbose_name
        self.assertEqual(project_verbose_name, "Project")
        project_help_text = ProjectImage._meta.get_field("project").help_text
        self.assertEqual(
            project_help_text,
            "Project to which this image belongs.",
        )
        project_on_delete = ProjectImage._meta.get_field("project")
        self.assertEqual(project_on_delete.remote_field.on_delete, d_db_models.CASCADE)
        project_related_name = ProjectImage._meta.get_field(
            "project"
        ).related_query_name()
        self.assertEqual(project_related_name, "images")

    # def test_project_uses_project_model(self):
    #     """
    #     `ProjectImage` model `project` field should use `Project` model.
    #     """
    #     project_field = ProjectImage._meta.get_field("project")
    #     self.assertEqual(project_field.related_model, Project)

    # def test_project_verbose_name(self):
    #     """
    #     `ProjectImage` model `project` field `verbose_name` should be
    #     "Project".
    #     """
    #     project_verbose_name = ProjectImage._meta.get_field(
    #         "project").verbose_name
    #     self.assertEqual(project_verbose_name, "Project")

    # def test_project_help_text(self):
    #     """
    #     `ProjectImage` model `project` field help text should be
    #     "Project to which this image belongs.".
    #     """
    #     project_help_text = ProjectImage._meta.get_field(
    #         "project").help_text
    #     self.assertEqual(
    #         project_help_text,
    #         "Project to which this image belongs.",
    #     )

    # def test_project_on_delete_cascade(self):
    #     """
    #     `ProjectImage` model `project` field `on_delete` should be
    #     `models.CASCADE`.
    #     """
    #     project_on_delete = ProjectImage._meta.get_field(
    #         "project")
    #     self.assertEqual(
    #         project_on_delete.remote_field.on_delete,
    #         d_db_models.CASCADE
    #     )

    # def test_project_related_name(self):
    #     """
    #     `ProjectImage` model `project` field related name should be `images`.
    #     """
    #     project_related_name = ProjectImage._meta.get_field(
    #         "project").related_query_name()
    #     self.assertEqual(project_related_name, "images")

    def test_image_field(self):
        """
        `ProjectImage` model `image` field should have the following
        attributes:

        - `verbose_name` should be "Image"
        - `help_text` should be "Add an image of the project."
        - `upload_to` should be "project_images/"
        """
        image_verbose_name = ProjectImage._meta.get_field("image").verbose_name
        self.assertEqual(image_verbose_name, "Image")
        image_help_text = ProjectImage._meta.get_field("image").help_text
        self.assertEqual(image_help_text, "Add an image of the project.")
        image_upload_to = ProjectImage._meta.get_field("image").upload_to
        self.assertEqual(image_upload_to, "project_images/")

    def test_caption_field(self):
        """
        `ProjectImage` model `caption` field should have the following
        attributes:

        - `verbose_name` should be "Caption"
        - `help_text` should be "Add a caption to the image."
        - `blank` should be "True"
        - `null` should be "True"
        """
        caption_verbose_name = ProjectImage._meta.get_field("caption").verbose_name
        self.assertEqual(caption_verbose_name, "Caption")
        caption_help_text = ProjectImage._meta.get_field("caption").help_text
        self.assertEqual(
            caption_help_text,
            "Add a caption to the image.",
        )
        caption_blank = ProjectImage._meta.get_field("caption").blank
        self.assertTrue(caption_blank)
        caption_null = ProjectImage._meta.get_field("caption").null
        self.assertTrue(caption_null)

    def test_dunder_string_method(self):
        """
        `ProjectImage` model `__str__` method should return `caption`.
        """
        project_image = ProjectImage.objects.create(
            project=Project.objects.create(
                owner=CustomUser.objects.create(
                    username="DezziKitten",
                    email="DezziKitten@purr.scratch",
                    password="MeowMeow42",
                ),
                title="DezziKitten's Test Project",
                description="Test Project Description",
            ),
            image="project_images/test_image.png",
            caption="Test Image Caption",
        )
        self.assertEqual(project_image.__str__(), "Test Image Caption")

    def test_meta_verbose_name_plural(self):
        """
        `ProjectImage` model `Meta` class `verbose_name_plural` should be
        "Project Images".
        """
        meta_verbose_name_plural = ProjectImage._meta.verbose_name_plural
        self.assertEqual(meta_verbose_name_plural, "Project Images")
