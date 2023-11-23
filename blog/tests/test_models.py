from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import models as d_db_models

from blog.models import Category, Post, Comment


class CategoryModelTest(TestCase):
    """
    Tests for the `Category` model.
    """

    def test_name_verbose_name(self):
        """
        `name` verbose_name should be 'Category Name'.
        """
        category_verbose_name = Category._meta.get_field("name").verbose_name
        self.assertEqual(category_verbose_name, "Category Name")

    def test_name_max_length(self):
        """
        `name` max_length should be 20.
        """
        category_max_length = Category._meta.get_field("name").max_length
        self.assertEqual(category_max_length, 20)

    def test_date_created_verbose_name(self):
        """
        `date_created` verbose_name should be 'Date the Category was created'.
        """
        date_created_verbose_name = Category._meta.get_field(
            "date_created"
        ).verbose_name
        self.assertEqual(date_created_verbose_name, "Date the Category was created")

    def test_date_created_auto_now_add_true(self):
        """
        `date_created` auto_now_add should be True.
        """
        date_created_auto_now_add = Category._meta.get_field(
            "date_created"
        ).auto_now_add
        self.assertTrue(date_created_auto_now_add)

    def test_dunder_string_method(self):
        """
        `__str__` method should return the name.
        """
        self.category = Category.objects.create(name="Test Category")
        self.assertEqual(str(self.category), "Test Category")

    def test_verbose_name_plural(self):
        """
        `verbose_name_plural` should be 'Categorie(s)'.
        """
        verbose_name_plural = Category._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "Categorie(s)")


class PostModelTest(TestCase):
    """
    Tests for the `Post` model.
    """

    def test_title_verbose_name(self):
        """
        `title` verbose_name should be 'Title of the Post'.
        """
        title_verbose_name = Post._meta.get_field("title").verbose_name
        self.assertEqual(title_verbose_name, "Title of the Post")

    def test_title_max_length(self):
        """
        `title` max_length should be 100.
        """
        title_max_length = Post._meta.get_field("title").max_length
        self.assertEqual(title_max_length, 100)

    def test_body_verbose_name(self):
        """
        `body` verbose_name should be 'Body of the Post'.
        """
        body_verbose_name = Post._meta.get_field("body").verbose_name
        self.assertEqual(body_verbose_name, "Body of the Post")

    def test_date_posted_verbose_name(self):
        """
        `date_posted` verbose_name should be 'Date the Post was posted'.
        """
        date_posted_verbose_name = Post._meta.get_field("date_posted").verbose_name
        self.assertEqual(date_posted_verbose_name, "Date the Post was posted")

    def test_date_posted_auto_now_add_true(self):
        """
        `date_posted` auto_now_add should be True.
        """
        date_posted_auto_now_add = Post._meta.get_field("date_posted").auto_now_add
        self.assertTrue(date_posted_auto_now_add)

    def test_author_uses_settings_auth_user_model(self):
        """
        `author` should use `config.settings.AUTH_USER_MODEL`
        (`CustomUser`).
        """
        author_field = Post._meta.get_field("author")
        self.assertEqual(author_field.related_model, get_user_model())

    def test_author_verbose_name(self):
        """
        `author` verbose_name should be 'Author of the Post'.
        """
        author_verbose_name = Post._meta.get_field("author").verbose_name
        self.assertEqual(author_verbose_name, "Author of the Post")

    def test_author_on_delete_cascade(self):
        """
        `author` on_delete should be CASCADE.
        """
        author_field = Post._meta.get_field("author")
        self.assertEqual(author_field.remote_field.on_delete, d_db_models.CASCADE)

    def test_categories_uses_category_model(self):
        """
        `categories` should use `blog.Category`.
        """
        categories_field = Post._meta.get_field("categories")
        self.assertEqual(categories_field.related_model, Category)

    def test_categories_related_name_is_posts(self):
        """
        `categories` related_name should be 'posts'.
        """
        categories_related_name = Post._meta.get_field(
            "categories"
        ).related_query_name()
        self.assertEqual(categories_related_name, "posts")

    def test_categories_blank_true(self):
        """
        `categories` blank should be True.
        """
        categories_blank = Post._meta.get_field("categories").blank
        self.assertTrue(categories_blank)

    def test_dunder_string_method(self):
        """
        `__str__` method should return the title.
        """
        self.author = get_user_model().objects.create_user(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        self.post = Post.objects.create(author=self.author, title="Test Post")
        self.assertEqual(str(self.post), "Test Post")

    def test_display_categories_method(self):
        """
        `display_categories` method should return a comma-separated list of
        first 4 `blog.Category` names.
        """
        self.author = get_user_model().objects.create_user(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        self.post = Post.objects.create(author=self.author, title="Test Post")
        self.category1 = Category.objects.create(name="Test Category 1")
        self.category2 = Category.objects.create(name="Test Category 2")
        self.category3 = Category.objects.create(name="Test Category 3")
        self.category4 = Category.objects.create(name="Test Category 4")
        self.post.categories.add(self.category1)
        self.post.categories.add(self.category2)
        self.post.categories.add(self.category3)
        self.post.categories.add(self.category4)
        self.assertEqual(
            self.post.display_categories(),
            ("Test Category 1, Test Category 2, " "Test Category 3, Test Category 4"),
        )

    def test_display_categories_short_description(self):
        """
        `display_categories` short_description should be 'Categories'.
        """
        display_categories_short_description = Post.display_categories.short_description
        self.assertEqual(display_categories_short_description, "Categories")

    def test_get_absolute_url_method(self):
        """
        `get_absolute_url` method should return the url to access a particular
        `blog.Post` instance.
        """
        self.author = get_user_model().objects.create_user(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        self.post = Post.objects.create(author=self.author, title="Test Post")
        self.assertEqual(self.post.get_absolute_url(), f"/blog/{self.post.pk}/")


class CommentModelTest(TestCase):
    """
    Tests for the `Comment` model.
    """

    def test_post_uses_post_model(self):
        """
        `post` should use `blog.Post`.
        """
        post_field = Comment._meta.get_field("post")
        self.assertEqual(post_field.related_model, Post)

    def test_post_related_name_is_comments(self):
        """
        `post` related_name should be 'comments'.
        """
        post_related_name = Comment._meta.get_field("post").related_query_name()
        self.assertEqual(post_related_name, "comments")

    def test_post_on_delete_cascade(self):
        """
        `post` on_delete should be CASCADE.
        """
        post_field = Comment._meta.get_field("post")
        self.assertEqual(post_field.remote_field.on_delete, d_db_models.CASCADE)

    def test_author_max_length(self):
        """
        `author` max_length should be 60.
        """
        author_max_length = Comment._meta.get_field("author").max_length
        self.assertEqual(author_max_length, 60)

    def test_body_verbose_name(self):
        """
        `body` verbose_name should be 'Body of the Comment'.
        """
        body_verbose_name = Comment._meta.get_field("body").verbose_name
        self.assertEqual(body_verbose_name, "Body of the Comment")

    def test_date_posted_verbose_name(self):
        """
        `date_posted` verbose_name should be 'Date the Comment was posted'.
        """
        date_posted_verbose_name = Comment._meta.get_field("date_posted").verbose_name
        self.assertEqual(date_posted_verbose_name, "Date the Comment was posted")

    def test_date_posted_auto_now_add_true(self):
        """
        `date_posted` auto_now_add should be True.
        """
        date_posted_auto_now_add = Comment._meta.get_field("date_posted").auto_now_add
        self.assertTrue(date_posted_auto_now_add)

    def test_dunder_string_method(self):
        """
        `__str__` method should return the body.
        """
        self.author = get_user_model().objects.create_user(
            username="DezziKitten",
            email="DezziKitten@meowmeow.scratch",
            password="MeowMeow42",
        )
        self.post_09_char = Post.objects.create(author=self.author, title="Test Post")
        self.post_23_char = Post.objects.create(
            author=self.author, title="Test Post - 23 chars"
        )
        self.assertEqual(str(self.post_09_char), "Test Post")
        self.assertEqual(str(self.post_23_char), "Test Post - 23 chars"[:20])
