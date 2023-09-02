"""App Urls"""

from django.urls import path, include


urlpatterns = [
    # API Endpoints
    path('api/', include('app.api.urls')),
]
