from django.contrib import admin

from blog.models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "date_posted",
        "display_categories",
    )
    list_filter = (
        "date_posted",
        "author",
        "categories",
    )
    search_fields = (
        "title",
        "body",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_created",
    )
    list_filter = (
        "name",
        "date_created",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "post",
        "date_posted",
    )
    list_filter = (
        "author",
        "post",
        "date_posted",
    )
    search_fields = (
        "author",
        "post",
        "date_posted",
    )
