"""Pet Serializers"""

from rest_framework import serializers

from app import models
from app.api.owner import owner_serializers


class PetSerializer(serializers.ModelSerializer):
    """Pet Serializer"""

    owner = owner_serializers.OwnerSerializer()

    class Meta:
        """Meta Class"""

        model = models.Pet
        fields = ("name", "owner")


class PetTagSerializer(serializers.ModelSerializer):
    """Pet Tag Serializer"""

    pet = PetSerializer()

    class Meta:
        """Meta Class"""

        model = models.PetTag
        fields = ("tag", "code", "pet")
