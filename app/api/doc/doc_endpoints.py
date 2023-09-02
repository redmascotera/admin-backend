"""API Endpoints"""

from django.views.generic import TemplateView, RedirectView
from django.shortcuts import reverse


class SwaggerView(TemplateView):
    """Swagger UI view"""
    template_name = 'swagger-ui.html'


class RootDocView(RedirectView):
    """Redirects to the default OpenAPI UI"""
    def get_redirect_url(self, *args, **kwargs):
        return reverse('swagger-ui')
