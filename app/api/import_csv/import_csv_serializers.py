from rest_framework import serializers


class ImportPetTagCSVRequest(serializers.Serializer):
    """Import CSV Request."""

    file = serializers.FileField()
