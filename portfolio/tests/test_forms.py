from django.test import TestCase

from portfolio.forms import ProjectForm
from portfolio.models import Project


class TestProjectForm(TestCase):
    """
    Test the `ProjectForm` form.
    """

    def test_meta_model(self):
        """
        Test that the `ProjectForm` form has the correct `Meta` class.
        """
        form = ProjectForm()
        self.assertEqual(form.Meta.model.__name__, 'Project')

    def test_meta_model_is_project(self):
        """
        Test that the `ProjectForm` form has the correct `Meta` class.
        """
        form = ProjectForm()
        self.assertEqual(form.Meta.model, Project)

    def test_project_form_meta_exclude(self):
        """
        Test that the `ProjectForm` form has the correct `Meta` class.
        """
        form = ProjectForm()
        self.assertEqual(form.Meta.exclude, ['owner'])
