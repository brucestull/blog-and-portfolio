from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Category, Post, Comment


class CategoryModelTest(TestCase):
    """
    Tests for the `Category` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Category.objects.create(
            name="Test Category",
        )

    # def __str__(self):
    #     return self.name
    def test_dunder_string(self):
        """
        `__str__` method should return the name.
        """
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), category.name)

    # max_length=20
    def test_name_max_length(self):
        """
        `name` max_length should be 20.
        """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field("name").max_length
        self.assertEqual(max_length, 20)

    # verbose_name='Word to describe the Category'
    def test_name_label(self):
        """
        `name` label should be 'Word to describe the Category'.
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Word to describe the Category")

    # verbose_name='Date the Category was created'
    def test_date_created_label(self):
        """
        `date_created` label should be 'Date the Category was created'.
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("date_created").verbose_name
        self.assertEqual(field_label, "Date the Category was created")

    # verbose_name_plural = 'categories'
    def test_verbose_name_plural(self):
        """
        `verbose_name_plural` should be 'categories'.
        """
        category = Category.objects.get(id=1)
        self.assertEqual(category._meta.verbose_name_plural, "categories")


class PostModelTest(TestCase):
    """
    Tests for the `Post` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        cls.author = get_user_model().objects.create_user(
            username="DezziKitten", password="MeowMeow42", email="Dezzi@BigCat.Meow"
        )

        cls.category_1 = Category.objects.create(name="Category 1")
        cls.category_2 = Category.objects.create(name="Category 2")
        cls.category_3 = Category.objects.create(name="Category 3")
        cls.category_4 = Category.objects.create(name="Category 4")
        cls.category_5 = Category.objects.create(name="Category 5")

        cls.post = Post.objects.create(
            title="Test Post",
            body="Test Body.",
            author=cls.author,
        )

        cls.post.categories.add(
            cls.category_1, cls.category_2, cls.category_3, cls.category_4, cls.category_5
        )

    def test_dunder_string(self):
        """
        `__str__` method should return the title.
        """
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), post.title)

    # verbose_name='Title of the Post'
    def test_title_label(self):
        """
        `title` label should be 'Title of the Post'.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "Title of the Post")

    # max_length=100
    def test_title_max_length(self):
        """
        `title` max_length should be 100.
        """
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    # verbose_name='Body of the Post'
    def test_body_label(self):
        """
        `body` label should be 'Body of the Post'.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("body").verbose_name
        self.assertEqual(field_label, "Body of the Post")

    # verbose_name='Date the Post was posted'
    def test_date_posted_label(self):
        """
        `date_posted` label should be 'Date the Post was posted'.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("date_posted").verbose_name
        self.assertEqual(field_label, "Date the Post was posted")

    #
    def test_author_label(self):
        """
        `author` label should be 'Author of the Post'.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "Author of the Post")

    def test_categories_label(self):
        """
        `categories` label should be 'categories'.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("categories").verbose_name
        self.assertEqual(field_label, "categories")

    def test_categories_related_name(self):
        """
        `categories` related_name attribute should be 'posts'.
        """
        post = Post.objects.get(id=1)
        related_name = post._meta.get_field("categories").related_query_name()
        self.assertEqual(related_name, "posts")

    def test_categories_blank(self):
        """
        `categories` blank attribute should be True.
        """
        post = Post.objects.get(id=1)
        blank = post._meta.get_field("categories").blank
        self.assertTrue(blank)

    def test_display_categories(self):
        self.assertEqual(
            self.post.display_categories(),
            "Category 1, Category 2, Category 3, Category 4",
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")


class CommentModelTest(TestCase):
    """
    Tests for the `Comment` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        cls.author = get_user_model().objects.create_user(
            username="DezziKitten", password="MeowMeow42", email="Dezzi@BigCat.Meow"
        )

        cls.category_1 = Category.objects.create(name="Category 1")
        cls.category_2 = Category.objects.create(name="Category 2")
        cls.category_3 = Category.objects.create(name="Category 3")
        cls.category_4 = Category.objects.create(name="Category 4")
        cls.category_5 = Category.objects.create(name="Category 5")

        cls.post = Post.objects.create(
            title="Test Post",
            body="Test Body.",
            author=cls.author,
        )

        cls.post.categories.add(
            cls.category_1, cls.category_2, cls.category_3, cls.category_4, cls.category_5
        )

        cls.comment_author = "Test Comment Author"
        cls.comment_body = "Test Comment Body That's Really Long"
        cls.comment = Comment.objects.create(
            post=cls.post, author=cls.comment_author, body=cls.comment_body
        )

    def test_dunder_string(self):
        """
        `__str__` method should return the first 20 characters of the `body` field.
        """
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), self.comment_body[:20])
