from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class TimestampMixin(models.Model):
    """
    Mixin class for `created_at` and `updated_at` fields.
    """

    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
    )

    class Meta:
        # This mixin class is not a model, so it should not be treated as such.
        # We don't want Django to create a table for this mixin class, that is
        # why we make it `abstract = True`
        abstract = True


class Technology(TimestampMixin):
    """
    A Technology class is created to store information about a technology.
    """

    name = models.CharField(
        verbose_name="Technology Name",
        help_text="Enter the name of the technology.",
        max_length=30,
    )
    description = models.TextField(
        verbose_name="Technology Description",
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
        verbose_name_plural = "Technologies"


class Project(TimestampMixin):
    """
    A Project class is created to store information about a project.
    """

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="Owner",
        help_text="Owner of this project.",
        on_delete=models.CASCADE,
        related_name="projects",
    )
    title = models.CharField(
        verbose_name="Project Title",
        help_text="Enter the title of the project.",
        max_length=100,
    )
    description = models.TextField(
        verbose_name="Project Description",
        help_text="Enter a description of the project.",
        blank=True,
        null=True,
    )
    technology = models.ManyToManyField(
        Technology,
        verbose_name="Technologies",
        help_text="Select a technology for this project.",
        related_name="projects",
    )
    main_image = models.ImageField(
        verbose_name="Main Image",
        help_text="Add an image of the project.",
        # `upload_to` is a required argument for `ImageField`.
        # It specifies the path to which the uploaded file will be saved.
        upload_to="portfolio/",
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
        Creates a string for the technologies. This will allow us to
        display multiple `Technology`'s in the `Project` list view.
        """
        # Limit the number of technologies to 3 and then join them with
        # a comma and a space to form a string.
        return ", ".join(
            technology.name for technology in self.technology.all()[:3]
        )


class ProjectImage(TimestampMixin):
    """
    Model for project images.
    """
    project = models.ForeignKey(
        Project,
        verbose_name="Project",
        help_text="Project to which this image belongs.",
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(
        verbose_name="Image",
        help_text="Add an image of the project.",
        upload_to="project_images/",
    )
    caption = models.CharField(
        verbose_name="Caption",
        help_text="Add a caption to the image.",
        max_length=100,
        blank=True,
        null=True,
    )
