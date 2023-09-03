"""API URLs"""
from django.urls import (
    path,
    include,
)
from rest_framework import routers

# Include JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Include all the api urls modules
from app.api.doc import doc_urls

# Include the viewsets that need to be registered in a router
from app.api.owner import owner_viewsets
from app.api.pet import pet_viewsets

# Create a router and register the viewsets
router = routers.SimpleRouter()
router.register("owners", owner_viewsets.OwnerViewSet, basename="owners")
router.register("pets", pet_viewsets.PetViewSet, basename="pets")
router.register("pet-tags", pet_viewsets.PetTagViewSet, basename="pet_tags")


# Include the api urls modules in the urlpatterns
urlpatterns = [
    path("docs/", include(doc_urls.urlpatterns)),
    # JWT Endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
# Include the router urls in the urlpatterns
urlpatterns.extend(router.urls)
