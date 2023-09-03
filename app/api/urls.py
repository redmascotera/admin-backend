"""API URLs"""
from django.urls import (
    path,
    include,
)

# Include JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Include all the api urls modules
from app.api.doc import doc_urls


# Include the api urls modules in the urlpatterns
urlpatterns = [
    path("docs/", include(doc_urls.urlpatterns)),
    # JWT Endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
