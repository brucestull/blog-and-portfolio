from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class Category(models.Model):
    """
    Model for `blog.Post` `blog.Category`.
    """

    name = models.CharField(
        max_length=20,
        verbose_name="Word to describe the Category",
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date the Category was created",
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for `blog.Post`.
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Title of the Post",
    )
    body = models.TextField(
        verbose_name="Body of the Post",
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date the Post was posted",
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Author of the Post",
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
        Returns a comma-separated list of `blog.Category` names.
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
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.CharField(
        max_length=60,
    )
    # author = models.ForeignKey(
    #     AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    body = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.body[:20]
