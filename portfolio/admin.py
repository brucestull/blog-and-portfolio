from django.contrib import admin

from portfolio.models import Technology, Project


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    """
    `ModelAdmin` class for the `Technology` model.
    """
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "name",
        "description",
        "created_at",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    `ModelAdmin` class for the `Project` model.
    """
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "title",
        "truncated_description",
        "display_technologies",
        "main_image",
        "created_at",
    )

    def truncated_description(self, obj):
        """
        Truncate `description` to 30 characters.
        """
        return obj.description[:30]
