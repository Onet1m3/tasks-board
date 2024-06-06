from rest_framework import serializers


__all__ = (
    'UploadResponseSuccessSchemas',
    'UploadResponseErrorSchemas',
)

class UploadResponseSuccessSchemas(serializers.Serializer):
    success = serializers.BooleanField(default=True)
    file_path = serializers.CharField()


class UploadResponseErrorSchemas(serializers.Serializer):
    success = serializers.BooleanField(default=False)
    error = serializers.CharField()