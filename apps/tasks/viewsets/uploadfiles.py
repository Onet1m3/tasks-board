from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema

from _core.utils.schemas.upload_response import UploadResponseErrorSchemas, UploadResponseSuccessSchemas
from apps.tasks.serializers import TaskFileSerializer

class UploadFileApiView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)
    serializer_class = TaskFileSerializer

    @extend_schema(
        responses={
            201: UploadResponseSuccessSchemas,
            400: UploadResponseErrorSchemas,
        },
        tags=["Task management"],
    )
    def post(self, request):
        request_data = self.request.data
        request_data.update({"user": request.user.id})
        serializer = TaskFileSerializer(data=request_data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": True, "file_path": serializer.data["file"]}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)