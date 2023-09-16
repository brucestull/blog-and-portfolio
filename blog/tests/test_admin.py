from django.test import TestCase

from blog.admin import (
    PostAdmin,
    CategoryAdmin,
    CommentAdmin,
)


class TestPostAdmin(TestCase):
    """
    Test `blog.admin.PostAdmin`.
    """

    def test_list_display(self):
        """
        Test `blog.admin.PostAdmin.list_display`.
        """
        self.assertEqual(
            PostAdmin.list_display,
            (
                "title",
                "author",
                "date_posted",
                "display_categories",
            ),
        )

    def test_list_filter(self):
        """
        Test `blog.admin.PostAdmin.list_filter`.
        """
        self.assertEqual(
            PostAdmin.list_filter,
            (
                "date_posted",
                "author",
                "categories",
            ),
        )

    def test_search_fields(self):
        """
        Test `blog.admin.PostAdmin.search_fields`.
        """
        self.assertEqual(
            PostAdmin.search_fields,
            (
                "title",
                "body",
            ),
        )


class TestCategoryAdmin(TestCase):
    """
    Test `blog.admin.CategoryAdmin`.
    """

    def test_list_display(self):
        """
        Test `blog.admin.CategoryAdmin.list_display`.
        """
        self.assertEqual(
            CategoryAdmin.list_display,
            (
                "name",
                "date_created",
            ),
        )

    def test_list_filter(self):
        """
        Test `blog.admin.CategoryAdmin.list_filter`.
        """
        self.assertEqual(
            CategoryAdmin.list_filter,
            (
                "name",
                "date_created",
            ),
        )


class TestCommentAdmin(TestCase):
    """
    Test `blog.admin.CommentAdmin`.
    """

    def test_list_display(self):
        """
        Test `blog.admin.CommentAdmin.list_display`.
        """
        self.assertEqual(
            CommentAdmin.list_display,
            (
                "author",
                "post",
                "date_posted",
            ),
        )

    def test_list_filter(self):
        """
        Test `blog.admin.CommentAdmin.list_filter`.
        """
        self.assertEqual(
            CommentAdmin.list_filter,
            (
                "author",
                "post",
                "date_posted",
            ),
        )

    def test_search_fields(self):
        """
        Test `blog.admin.CommentAdmin.search_fields`.
        """
        self.assertEqual(
            CommentAdmin.search_fields,
            (
                "author",
                "post",
                "date_posted",
            ),
        )
