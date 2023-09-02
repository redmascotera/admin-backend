"""Django URLs for API Endpoints"""

from django.urls import path
from rest_framework.schemas import get_schema_view

from app.api import endpoints


urlpatterns = [
    # Auto Generated OpenAPI Schema
    path('openapi-schema/', get_schema_view(
        title="Red Mascotera API",
        description="API Endpoints for Red Mascotera",
        version="1.0.0"
    ), name='openapi-schema'),
    # Swagger View
    path('swagger/', endpoints.SwaggerView.as_view(), name='swagger-ui'),
]
