"""Django URLs for API Endpoints"""

from django.urls import path
from rest_framework.schemas import get_schema_view

from app.api.doc import doc_endpoints

urlpatterns = [
    # Auto Generated OpenAPI Schema
    path(
        "openapi/",
        get_schema_view(
            title="Red Mascotera API",
            description="API Endpoints for Red Mascotera",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    # Swagger View
    path("swagger/", doc_endpoints.SwaggerView.as_view(), name="swagger-ui"),
    # Root View
    path("", doc_endpoints.RootDocView.as_view(), name="docs"),
]
