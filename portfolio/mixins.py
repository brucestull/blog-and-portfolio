from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse


class RegistrationAcceptedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return redirect("login")
        if not request.user.registration_accepted:
            portfolio_projects_url = reverse("portfolio:projects")
            return HttpResponse(
                f"Registration not accepted yet. "
                f"Please check out the projects at "
                f"<a href='{portfolio_projects_url}'>"
                f"FlynntKnapp Projects"
                f"</a>"
            )
        return super().dispatch(request, *args, **kwargs)
