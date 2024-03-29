# Generated by Django 4.1.9 on 2023-09-23 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "portfolio",
            "0006_alter_technology_options_alter_project_created_at_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Add an image of the project.",
                        upload_to="project_images/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for this image.",
                        max_length=100,
                        null=True,
                        verbose_name="Caption",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project to which this image belongs.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="portfolio.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
