"""Pet Serializers"""

from rest_framework import serializers

from app import models
from app.api.owner import owner_serializers


class PetSerializer(serializers.ModelSerializer):
    """Pet Serializer"""

    owner = owner_serializers.OwnerSerializer(allow_null=True, required=False, default=None)
    owner_id = serializers.IntegerField(write_only=True, required=False, default=None)

    class Meta:
        """Meta Class"""

        model = models.Pet
        fields = ("id", "name", "owner", "owner_id")
        read_only_fields = ("id", "owner")


class PetTagSerializer(serializers.ModelSerializer):
    """Pet Tag Serializer"""

    pet = PetSerializer(allow_null=True, required=False, default=None)
    pet_id = serializers.IntegerField(write_only=True, required=False, default=None)

    class Meta:
        """Meta Class"""

        model = models.PetTag
        fields = ("id", "tag", "code", "pet", "pet_id")
        read_only_fields = ("id", "pet")
