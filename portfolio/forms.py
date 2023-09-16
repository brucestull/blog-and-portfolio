from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """
    Override the default form for the `Project` model.

    We are doing this so we can exclude the `owner` field from the update
    view.
    """
    class Meta:
        model = Project
        exclude = ['owner']
