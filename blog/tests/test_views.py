from django.test import TestCase
from django.urls import reverse

from blog.models import (
    Category,
    Post,
    Comment
)

from accounts.models import CustomUser


class BlogIndexViewTest(TestCase):
    """
    Test the `blog_index` view.
    """

    def test_blog_index_view_url_exists_at_desired_location(self):
        """
        Test that the `blog_index` view is rendered at the desired location.
        """
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_blog_index_view_url_accessible_by_name(self):
        """
        Test that the `blog_index` view is rendered at the desired location
        by name.
        """
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def test_blog_index_view_uses_correct_template(self):
        """
        Test that the `blog_index` view uses the correct template.
        """
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_index.html")

    def test_blog_index_view_uses_correct_context(self):
        """
        Test that the `blog_index` view uses the correct context.
        """
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["the_site_name"], "FlynntKnapp")
        self.assertEqual(response.context["page_title"], "Knappings")


class BlogCategoryViewTest(TestCase):
    """
    Test the `blog_category` view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a `Post` object for use in testing.
        """
        cls.author_01 = CustomUser.objects.create_user(
            username="testuser01",
            password="testpass01",
        )
        cls.test_category_01 = Category.objects.create(name="Test Category 01")
        cls.test_category_02 = Category.objects.create(name="Test Category 02")
        cls.test_post_01 = Post.objects.create(
            title="Test Post Title",
            body="Test Post Body",
            author_id=cls.author_01.id,
        )
        cls.test_post_01.categories.add(cls.test_category_01)
        cls.test_post_01.categories.add(cls.test_category_02)

    def test_blog_category_view_url_exists_at_desired_location(self):
        """
        Test that the `blog_category` view is rendered at the desired
        location.
        """
        response = self.client.get(
            f"/blog/{self.test_category_01.name}/")
        self.assertEqual(response.status_code, 200)

    def test_blog_category_view_url_accessible_by_name(self):
        """
        Test that the `blog_category` view is rendered at the desired
        location by name.
        """
        response = self.client.get(
            reverse(
                "blog:blog-category",
                kwargs={'category': self.test_category_01.name})
        )
        self.assertEqual(response.status_code, 200)

    def test_blog_category_view_uses_correct_template(self):
        """
        Test that the `blog_category` view uses the correct template.
        """
        response = self.client.get(
            reverse(
                "blog:blog-category",
                kwargs={'category': self.test_category_01.name})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_category.html")

    def test_blog_category_view_uses_correct_context(self):
        """
        Test that the `blog_category` view uses the correct context.
        """
        response = self.client.get(
            reverse(
                "blog:blog-category",
                kwargs={'category': self.test_category_01.name})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["the_site_name"], "FlynntKnapp")
        self.assertEqual(response.context["page_title"], "Flynnt Knappings")

    def test_blog_category_view_returns_correct_queryset(self):
        """
        Test that the `blog_category` view returns the correct queryset.
        """
        response = self.client.get(
            reverse(
                "blog:blog-category",
                kwargs={'category': self.test_category_01.name})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["category"], self.test_category_01.name)
        self.assertEqual(
            response.context["posts"][0].title, self.test_post_01.title)


class BlogDetailViewTest(TestCase):
    """
    Test the `blog_detail` view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a `Post` object for use in testing.
        """
        cls.author_01 = CustomUser.objects.create_user(
            username="testuser01",
            password="testpass01",
        )
        cls.test_category_01 = Category.objects.create(name="Test Category 01")
        cls.test_category_02 = Category.objects.create(name="Test Category 02")
        cls.test_post_01 = Post.objects.create(
            title="Test Post Title",
            body="Test Post Body",
            author_id=cls.author_01.id,
        )

    def test_blog_detail_view_url_exists_at_desired_location(self):
        """
        Test that the `blog_detail` view is rendered at the desired location.
        """
        response = self.client.get(
            f"/blog/{self.test_post_01.id}/")
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_view_url_accessible_by_name(self):
        """
        Test that the `blog_detail` view is rendered at the desired location
        by name.
        """
        response = self.client.get(
            reverse("blog:blog-detail", kwargs={'pk': self.test_post_01.id}))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_view_post_method_adds_comment(self):
        """
        Test that the `blog_detail` view adds a `Comment` object when
        submitted via POST.
        """
        self.client.login(
            username=self.author_01.username,
            password="testpass01",
        )
        response = self.client.post(
            reverse("blog:blog-detail", kwargs={'pk': self.test_post_01.id}),
            data={
                "author": "Test Author",
                "body": "Test Comment Body",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Comment.objects.filter(
                author="Test Author",
                body="Test Comment Body",
                post=self.test_post_01,
            ).count(),
            1,
        )

    def test_blog_detail_view_uses_correct_template(self):
        """
        Test that the `blog_detail` view uses the correct template.
        """
        response = self.client.get(
            reverse("blog:blog-detail", kwargs={'pk': self.test_post_01.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_detail.html")

    def test_blog_detail_view_uses_correct_context(self):
        """
        Test that the `blog_detail` view uses the correct context.
        """
        response = self.client.get(
            reverse("blog:blog-detail", kwargs={'pk': self.test_post_01.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["the_site_name"], "FlynntKnapp")
        self.assertEqual(response.context["page_title"], "Knappings")
        self.assertEqual(
            response.context["post"].title, self.test_post_01.title)
        # TODO: Add test for context "form" key.

    def test_blog_detail_view_returns_correct_queryset(self):
        """
        Test that the `blog_detail` view returns the correct queryset.
        """
        response = self.client.get(
            reverse("blog:blog-detail", kwargs={'pk': self.test_post_01.id}))
        self.assertEqual(response.status_code, 200)
