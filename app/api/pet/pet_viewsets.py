"""Pet ViewSets"""

from rest_framework import viewsets

from app import models
from app.api.pet import pet_serializers


class PetViewSet(viewsets.ModelViewSet):
    """Pet view set"""

    serializer_class = pet_serializers.PetSerializer

    def get_queryset(self):
        """Returns the queryset filtered by the user"""
        queryset = models.Pet.objects.all()
        return queryset

    def perform_create(self, serializer):
        """Creates a new pet"""
        serializer.save()


class PetTagViewSet(viewsets.ModelViewSet):
    """Pet Tag view set"""

    serializer_class = pet_serializers.PetTagSerializer

    def get_queryset(self):
        """Returns the queryset filtered by the user"""
        queryset = models.PetTag.objects.all()
        return queryset

    def perform_create(self, serializer):
        """Creates a new pet tag"""
        serializer.save()
