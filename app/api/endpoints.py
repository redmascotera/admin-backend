"""API Endpoints"""

from django.views.generic import TemplateView


class SwaggerView(TemplateView):
    """Swagger UI view"""
    template_name = 'swagger-ui.html'
