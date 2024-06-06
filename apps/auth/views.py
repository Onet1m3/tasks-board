from rest_framework.views import APIView, Response, status
from drf_spectacular.utils import extend_schema

from apps.auth.serializers import UserSignUpSerializer
from _core.utils import SimpleResponseSuccessSchemas, SimpleResponseErrorSchemas


__all__ = (
    'UserSignUp',
)


class UserSignUp(APIView):

    @extend_schema(
        request=UserSignUpSerializer,
        responses={
            201: SimpleResponseSuccessSchemas,
            400: SimpleResponseErrorSchemas
        },
        tags=["User"],
    )
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "msg": "User created"}, status=status.HTTP_201_CREATED)
        
        return Response({"success": False, "msg": f'{serializer._errors}'}, status=status.HTTP_400_BAD_REQUEST)
