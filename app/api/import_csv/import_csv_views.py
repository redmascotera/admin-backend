"""Import CSV Views."""

from drf_yasg.utils import swagger_auto_schema

from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.api.import_csv.import_csv_actions import import_csv_file
from app.api.import_csv.import_csv_serializers import ImportPetTagCSVRequest


class ImportPetTagCSVView(APIView):
    """Import CSV Endpoint."""

    parser_classes = (FileUploadParser,)

    @swagger_auto_schema(request_body=ImportPetTagCSVRequest)
    def put(self, request):
        """Handle HTTP POST request."""
        serializer = ImportPetTagCSVRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        import_csv_file(serializer.validated_data["file"])

        return Response(status=status.HTTP_204_NO_CONTENT)
