from django.db import models
from django.urls import reverse

from config.settings import AUTH_USER_MODEL


class Category(models.Model):
    """
    Model for `blog.Post` `blog.Category`.
    """

    name = models.CharField(
        verbose_name="Category Name",
        max_length=20,
    )
    date_created = models.DateTimeField(
        verbose_name="Date the Category was created",
        auto_now_add=True,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for `blog.Post`.
    """

    title = models.CharField(
        verbose_name="Title of the Post",
        max_length=100,
    )
    body = models.TextField(
        verbose_name="Body of the Post",
    )
    date_posted = models.DateTimeField(
        verbose_name="Date the Post was posted",
        auto_now_add=True,
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="Author of the Post",
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(
        Category,
        related_name="posts",
        blank=True,
    )

    def __str__(self):
        return self.title

    def display_categories(self):
        """
        Returns a comma-separated list of first 4 `blog.Category` names.
        """
        return ", ".join([category.name for category in self.categories.all()[:4]])

    display_categories.short_description = "Categories"

    def get_absolute_url(self):
        """
        Returns the url to access a particular `blog.Post` instance.
        """
        return reverse("blog:blog-detail", args=[str(self.id)])


class Comment(models.Model):
    """
    Model for `blog.Post` `blog.Comment`.
    """

    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    author = models.CharField(
        # TODO: Add `AUTH_USER_MODEL` relationship so only authenticated
        # users can comment.
        max_length=60,
    )
    body = models.TextField(
        verbose_name="Body of the Comment",
    )
    date_posted = models.DateTimeField(
        verbose_name="Date the Comment was posted",
        auto_now_add=True,
    )

    def __str__(self):
        return self.body[:20]
