"""Owners ViewSet"""

from rest_framework import (
    # permissions,
    viewsets,
)

from app.api.owner import owner_serializers
from app.models import Owner


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner view set"""

    serializer_class = owner_serializers.OwnerSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Returns the queryset filtered by the user"""
        queryset = Owner.objects.all()
        return queryset

    def perform_create(self, serializer):
        """Creates a new owner"""
        serializer.save()
