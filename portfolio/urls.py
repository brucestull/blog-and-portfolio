from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path(
        "projects/",
        views.ProjectListView.as_view(),
        name="projects",
    ),
    path(
        "projects/create/",
        views.ProjectCreateView.as_view(),
        name="project-create",
    ),
    path(
        "projects/<int:pk>/update/",
        views.ProjectUpdateView.as_view(),
        name="project-update",
    ),
    path(
        "projects/<int:pk>/",
        views.ProjectDetailView.as_view(),
        name="project-detail",
    ),
    path(
        "technologies/<int:technology_id>/projects/",
        views.technology_projects,
        name="technology-projects",
    )
]
