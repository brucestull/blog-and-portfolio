from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import ProjectForm
from config.settings.common import THE_SITE_NAME
from . import models


class ProjectCreateView(CreateView):
    """
    Create view for `models.Project` model.
    """

    model = models.Project
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Project"
        context["the_site_name"] = THE_SITE_NAME
        return context


class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    """
    Update view for `models.Project` model.
    """

    model = models.Project
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Project"
        context["the_site_name"] = THE_SITE_NAME
        return context

    def test_func(self):
        """
        Only allow the user who created the project to update it.
        """
        return self.request.user == self.get_object().owner


class ProjectDetailView(DetailView):
    """
    Detail view for `models.Project` model.
    """

    model = models.Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class ProjectListView(ListView):
    """
    List view for `models.Project` model.
    """

    queryset = models.Project.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Projects"
        context["the_site_name"] = THE_SITE_NAME
        return context
