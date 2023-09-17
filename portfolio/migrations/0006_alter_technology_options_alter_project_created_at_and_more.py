# Generated by Django 4.1.9 on 2023-09-17 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("portfolio", "0005_alter_project_main_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="technology",
            options={"verbose_name_plural": "Technologies"},
        ),
        migrations.AlterField(
            model_name="project",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Enter a description of the project.",
                null=True,
                verbose_name="Project Description",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                help_text="Owner of this project.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Owner",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="technology",
            field=models.ManyToManyField(
                help_text="Select a technology for this project.",
                related_name="projects",
                to="portfolio.technology",
                verbose_name="Technologies",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(
                help_text="Enter the title of the project.",
                max_length=100,
                verbose_name="Project Title",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated At"),
        ),
        migrations.AlterField(
            model_name="technology",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
        ),
        migrations.AlterField(
            model_name="technology",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Enter a description of the technology.",
                null=True,
                verbose_name="Technology Description",
            ),
        ),
        migrations.AlterField(
            model_name="technology",
            name="name",
            field=models.CharField(
                help_text="Enter the name of the technology.",
                max_length=30,
                verbose_name="Technology Name",
            ),
        ),
        migrations.AlterField(
            model_name="technology",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated At"),
        ),
    ]
