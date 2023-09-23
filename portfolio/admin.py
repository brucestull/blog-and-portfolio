from django.contrib import admin

from portfolio.models import Technology, Project, ProjectImage


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    """
    `ModelAdmin` class for the `Technology` model.
    """
    list_display = (
        "name",
        "description",
        "created_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    `ModelAdmin` class for the `Project` model.
    """
    list_display = (
        "title",
        "truncated_description",
        "display_technologies",
        "main_image",
        "created_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def truncated_description(self, obj):
        """
        Truncate `description` to 30 characters.
        """
        return obj.description[:30]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    """
    `ModelAdmin` class for the `ProjectImage` model.
    """
    list_display = (
        "project",
        "image",
        "caption",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
