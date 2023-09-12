"""Owner Serializers"""

from rest_framework import serializers

from app.models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    """Owner Serializer"""

    class Meta:
        """Meta Class"""

        model = Owner
        fields = ("id", "name", "email", "phone", "alt_phone")
        read_only_fields = ("id",)
