from django.test import TestCase

from accounts.models import CustomUser
from portfolio.models import (TimestampMixin, Technology, Project,)

TEST_TECHNOLOGY_NAME_LABEL = "name"
TEST_TECHNOLOGY_NAME_HELP_TEXT = "Enter the name of the technology."
TEST_TECHNOLOGY_NAME_MAX_LENGTH = 30

TEST_TECHNOLOGY_DESCRIPTION_LABEL = "description"
TEST_TECHNOLOGY_DESCRIPTION_HELP_TEXT = "Enter a description of the technology."

TEST_TECHNOLOGY_VERBOSE_NAME_PLURAL = "technologies"

TEST_TECHNOLOGY_NAME_ONE = "Django"
TEST_TECHNOLOGY_DESCRIPTION_ONE = "Django Web Framework"
TEST_TECHNOLOGY_NAME_TWO = "Python"
TEST_TECHNOLOGY_DESCRIPTION_TWO = "Python Programming Language"
TEST_TECHNOLOGY_NAME_THREE = "PostgreSQL"
TEST_TECHNOLOGY_DESCRIPTION_THREE = "PostgreSQL Database Management System"
TEST_TECHNOLOGY_NAME_FOUR = "HTML"
TEST_TECHNOLOGY_DESCRIPTION_FOUR = "HTML Markup Language"


TEST_PROJECT_OWNER_LABEL = "owner"
TEST_PROJECT_OWNER_HELP_TEXT = "Owner of this project."
TEST_PROJECT_OWNER_RELATED_NAME = "projects"

TEST_PROJECT_TITLE_LABEL = "title"
TEST_PROJECT_TITLE_MAX_LENGTH = 100

TEST_PROJECT_DESCRIPTION_LABEL = "description"
TEST_PROJECT_DESCRIPTION_HELP_TEXT = "Enter a description of the project."

TEST_PROJECT_TECHNOLOGY_LABEL = "technology"
TEST_PROJECT_TECHNOLOGY_HELP_TEXT = "Select a technology for this project."
TEST_PROJECT_TECHNOLOGY_VERBOSE_NAME = "technologies"
TEST_PROJECT_TECHNOLOGY_RELATED_NAME = "projects"

TEST_PROJECT_IMAGE_LABEL = "image"
TEST_PROJECT_IMAGE_HELP_TEXT = "Add an image of the project."
TEST_PROJECT_IMAGE_PATH = "/img"

TEST_PROJECT_TITLE = "Test Project"
TEST_PROJECT_DESCRIPTION = "Test description."
TEST_PROJECT_TECHNOLOGY = "Django"
TEST_PROJECT_IMAGE = "test_image.jpg"


class TimestampMixinTest(TestCase):
    """
    Tests for `TimestampMixin` model.
    """

    def test_created_at_label(self):
        """
        `TimestampMixin` model `created_at` field label should be `created at`.
        """
        field_label = TimestampMixin._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")

    def test_created_at_auto_now_add_true(self):
        """
        `TimestampMixin` model `created_at` field `auto_now_add` should be `True`.
        """
        auto_now_add = TimestampMixin._meta.get_field(
            "created_at").auto_now_add
        self.assertTrue(auto_now_add)

    def test_updated_at_label(self):
        """
        `TimestampMixin` model `updated_at` field label should be `updated at`.
        """
        field_label = TimestampMixin._meta.get_field("updated_at").verbose_name
        self.assertEqual(field_label, "updated at")

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

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.technology = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_ONE,
            description=TEST_TECHNOLOGY_DESCRIPTION_ONE,
        )

    def test_name_label(self):
        """
        `Technology` model `name` field label should be `name`.
        """
        field_label = self.technology._meta.get_field(
            TEST_TECHNOLOGY_NAME_LABEL
        ).verbose_name
        self.assertEqual(field_label, TEST_TECHNOLOGY_NAME_LABEL)

    def test_name_help_text(self):
        """
        `Technology` model `name` field help text should be `Enter the name of the technology.`.
        """
        field_help_text = self.technology._meta.get_field(
            TEST_TECHNOLOGY_NAME_LABEL
        ).help_text
        self.assertEqual(field_help_text, TEST_TECHNOLOGY_NAME_HELP_TEXT)

    def test_name_max_length(self):
        """
        `Technology` model `name` field max length should be 30.
        """
        max_length = self.technology._meta.get_field(
            TEST_TECHNOLOGY_NAME_LABEL
        ).max_length
        self.assertEqual(max_length, TEST_TECHNOLOGY_NAME_MAX_LENGTH)

    def test_description_label(self):
        """
        `Technology` model `description` field label should be `description`.
        """
        field_label = self.technology._meta.get_field(
            TEST_TECHNOLOGY_DESCRIPTION_LABEL
        ).verbose_name
        self.assertEqual(field_label, TEST_TECHNOLOGY_DESCRIPTION_LABEL)

    def test_description_help_text(self):
        """
        `Technology` model `description` field help text should be
        `Enter a description of the technology.`.
        """
        field_help_text = self.technology._meta.get_field(
            TEST_TECHNOLOGY_DESCRIPTION_LABEL
        ).help_text
        self.assertEqual(
            field_help_text, TEST_TECHNOLOGY_DESCRIPTION_HELP_TEXT)

    def test_dunder_string_method(self):
        """
        `Technology` model `__str__` method should return `name`.
        """
        self.assertEqual(str(self.technology), TEST_TECHNOLOGY_NAME_ONE)

    def test_meta_verbose_name_plural(self):
        """
        `Technology` model `Meta` class `verbose_name_plural` should be `technologies`.
        """
        field_verbose_name_plural = self.technology._meta.verbose_name_plural
        self.assertEqual(
            field_verbose_name_plural,
            TEST_TECHNOLOGY_VERBOSE_NAME_PLURAL,
        )
        # Another way to test this is to use the `Technology` model class itself.
        self.assertEqual(
            str(Technology._meta.verbose_name_plural),
            TEST_TECHNOLOGY_VERBOSE_NAME_PLURAL,
        )


class ProjectTest(TestCase):
    """
    Tests for `Project` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            email="testemail",
            password="testpassword",
        )
        cls.technology = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_ONE,
            description=TEST_TECHNOLOGY_DESCRIPTION_ONE,
        )

        cls.project = Project.objects.create(
            owner=cls.user,
            title=TEST_PROJECT_TITLE,
            description=TEST_PROJECT_DESCRIPTION,
            main_image=TEST_PROJECT_IMAGE,
        )
        cls.project.technology.set([cls.technology])

    def test_owner_label(self):
        """
        `Project` model `owner` field label should be `owner`.
        """
        field_label = self.project._meta.get_field(
            TEST_PROJECT_OWNER_LABEL
        ).verbose_name
        self.assertEqual(field_label, TEST_PROJECT_OWNER_LABEL)

    def test_owner_help_text(self):
        """
        `Project` model `owner` field help text should be `Owner of this project.`.
        """
        field_help_text = self.project._meta.get_field(
            TEST_PROJECT_OWNER_LABEL
        ).help_text
        self.assertEqual(field_help_text, TEST_PROJECT_OWNER_HELP_TEXT)

    def test_owner_related_name(self):
        """
        `Project` model `owner` field related name should be `projects`.
        """
        related_name = self.project._meta.get_field(
            TEST_PROJECT_OWNER_LABEL
        ).related_query_name()
        self.assertEqual(related_name, TEST_PROJECT_OWNER_RELATED_NAME)

    def test_title_label(self):
        """
        `Project` model `title` field label should be `title`.
        """
        field_label = self.project._meta.get_field(
            TEST_PROJECT_TITLE_LABEL
        ).verbose_name
        self.assertEqual(field_label, TEST_PROJECT_TITLE_LABEL)

    def test_title_max_length(self):
        """
        `Project` model `title` field max length should be 100.
        """
        max_length = self.project._meta.get_field(
            TEST_PROJECT_TITLE_LABEL).max_length
        self.assertEqual(max_length, TEST_PROJECT_TITLE_MAX_LENGTH)

    def test_description_label(self):
        """
        `Project` model `description` field label should be `description`.
        """
        field_label = self.project._meta.get_field(
            TEST_PROJECT_DESCRIPTION_LABEL
        ).verbose_name
        self.assertEqual(field_label, TEST_PROJECT_DESCRIPTION_LABEL)

    def test_description_help_text(self):
        """
        `Project` model `description` field help text should be `Enter a description of the project.`.
        """
        help_text = self.project._meta.get_field(
            TEST_PROJECT_DESCRIPTION_LABEL
        ).help_text
        self.assertEqual(help_text, TEST_PROJECT_DESCRIPTION_HELP_TEXT)

    def test_technology_label(self):
        """
        `Project` model `technology` field label should be `technology`.
        """
        field_label = self.project._meta.get_field(
            TEST_PROJECT_TECHNOLOGY_LABEL,
        ).verbose_name
        self.assertEqual(field_label, TEST_PROJECT_TECHNOLOGY_VERBOSE_NAME)

    def test_technology_help_text(self):
        """
        `Project` model `technology` field help text should be `Enter the technology used in the project.`.
        """
        help_text = self.project._meta.get_field(
            TEST_PROJECT_TECHNOLOGY_LABEL,
        ).help_text
        self.assertEqual(help_text, TEST_PROJECT_TECHNOLOGY_HELP_TEXT)

    def test_main_image_field(self):
        """
        `Project` model `main_image` field should have the following attributes:

        - `verbose_name` should be "Main Image"
        - `help_text` should be "Add an image of the project."
        - `upload_to` should be "portfolio/"
        - `blank` should be "True"
        - `null` should be "True"
        """
        main_image_verbose_name = self.project._meta.get_field(
            "main_image"
        ).verbose_name
        self.assertEqual(main_image_verbose_name, "Main Image")
        main_image_help_text = self.project._meta.get_field(
            "main_image"
        ).help_text
        self.assertEqual(main_image_help_text, "Add an image of the project.")
        main_image_upload_to = self.project._meta.get_field(
            "main_image"
        ).upload_to
        self.assertEqual(main_image_upload_to, "portfolio/")
        main_image_blank = self.project._meta.get_field(
            "main_image"
        ).blank
        self.assertTrue(main_image_blank)
        main_image_null = self.project._meta.get_field(
            "main_image"
        ).null
        self.assertTrue(main_image_null)

    # TODO: Fix this test.
    # def test_image_path(self):
    #     """
    #     `Project` model `image` field path should be `/img`.
    #     """
    #     path = self.project._meta.get_field(TEST_PROJECT_IMAGE_LABEL).path
    #     self.assertEqual(path, PROJECT_IMAGE_PATH)

    def test_created_at_label(self):
        """
        `Project` model `created_at` field label should be `created at`.
        """
        field_label = self.project._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")

    def test_created_at_auto_now_add_attribute_true(self):
        """
        `Project` model `created_at` field should have `auto_now_add=True`.
        """
        auto_now_add = self.project._meta.get_field("created_at").auto_now_add
        self.assertTrue(auto_now_add)

    def test_updated_at_label(self):
        """
        `Project` model `updated_at` field label should be `updated at`.
        """
        field_label = self.project._meta.get_field("updated_at").verbose_name
        self.assertEqual(field_label, "updated at")

    def test_updated_at_auto_now_attribute_true(self):
        """
        `Project` model `updated_at` field should have `auto_now=True`.
        """
        auto_now = self.project._meta.get_field("updated_at").auto_now
        self.assertTrue(auto_now)

    def test_dunder_string_method(self):
        """
        `Project` model `__str__` method should return `title`.
        """
        self.assertEqual(self.project.__str__(), TEST_PROJECT_TITLE)

    def test_display_technologies_method_with_one_technology(self):
        """
        `Project` model `display_technologies` method should return `technology.name`.
        """
        self.assertEqual(
            self.project.display_technologies(),
            TEST_TECHNOLOGY_NAME_ONE,
        )

    def test_display_technologies_method_with_two_technologies(self):
        """
        `Project` model `display_technologies` method should return `technology.name, technology.name`.
        """
        technology_two = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_TWO,
            description=TEST_TECHNOLOGY_DESCRIPTION_TWO,
        )
        self.project.technology.set([self.technology, technology_two])
        self.assertEqual(
            self.project.display_technologies(),
            f"{TEST_TECHNOLOGY_NAME_ONE}, {TEST_TECHNOLOGY_NAME_TWO}",
        )

    def test_display_technologies_method_with_four_technologies(self):
        """
        `Project` model `display_technologies` method should return the first three technologies if there are more than three.
        """
        technology_two = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_TWO,
            description=TEST_TECHNOLOGY_DESCRIPTION_TWO,
        )
        technology_three = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_THREE,
            description=TEST_TECHNOLOGY_DESCRIPTION_THREE,
        )
        technology_four = Technology.objects.create(
            name=TEST_TECHNOLOGY_NAME_FOUR,
            description=TEST_TECHNOLOGY_DESCRIPTION_FOUR,
        )
        self.project.technology.set(
            [self.technology, technology_two, technology_three, technology_four]
        )
        self.assertEqual(
            self.project.display_technologies(),
            f"{TEST_TECHNOLOGY_NAME_ONE}, {TEST_TECHNOLOGY_NAME_TWO}, {TEST_TECHNOLOGY_NAME_THREE}",
        )
