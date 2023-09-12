"""Django URLs for API Endpoints"""

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.api.doc import doc_endpoints

SchemaView = get_schema_view(
    openapi.Info(
        title="RedMascotera Admin API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Auto Generated OpenAPI Schema
    path("swagger<format>/", SchemaView.without_ui(cache_timeout=0), name="schema-json"),  # noqa
    path(
        "swagger/", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"  # noqa
    ),
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),  # noqa
    # Root View
    path("", doc_endpoints.RootDocView.as_view(), name="docs"),
]
