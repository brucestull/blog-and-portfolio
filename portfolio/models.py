from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class TimestampMixin(models.Model):
    """
    Mixin class for `created_at` and `updated_at` fields.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        # This mixin class is not a model, so it should not be treated as such.
        # We don't want Django to create a table for this mixin class, that is
        # why we make it `abstract = True`
        abstract = True


class Technology(TimestampMixin, models.Model):
    """
    A Technology class is created to store information about a technology.
    """

    name = models.CharField(
        help_text="Enter the name of the technology.",
        max_length=30,
    )
    description = models.TextField(
        help_text="Enter a description of the technology.",
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        String representation of Technology.
        """
        return self.name

    class Meta:
        verbose_name_plural = "technologies"


class Project(TimestampMixin, models.Model):
    """
    A Project class is created to store information about a project.
    """

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        help_text="Owner of this project.",
        on_delete=models.CASCADE,
        related_name="projects",
    )
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        help_text="Enter a description of the project.",
        blank=True,
        null=True,
    )
    technology = models.ManyToManyField(
        Technology,
        help_text="Select a technology for this project.",
        verbose_name="technologies",
        related_name="projects",
    )
    image = models.ImageField(
        help_text="Add an image of the project.",
        # `upload_to` is a required argument for `ImageField`.
        # It specifies the path to which the uploaded file will be saved.
        # upload_to="media/",
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        String representation of Project.
        """
        return self.title

    def get_absolute_url(self):
        return reverse(
            "portfolio:project-detail",
            kwargs={"pk": self.pk},
        )

    def display_technologies(self):
        """
        Creates a string for the technologies. This will allow us to display multiple `Technology`'s in the `Project` list view.
        """
        # Limit the number of technologies to 3 and then join them with a comma and a space to form a string.
        return ", ".join(technology.name for technology in self.technology.all()[:3])
