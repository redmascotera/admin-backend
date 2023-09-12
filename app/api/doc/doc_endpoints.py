"""API Endpoints"""

from django.views.generic import RedirectView
from django.shortcuts import reverse


class RootDocView(RedirectView):
    """Redirects to the default OpenAPI UI"""

    def get_redirect_url(self):
        return reverse("schema-swagger-ui")
