from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import CreateSessionSerializer
from .stripe_session import create_session


class CreateSessionView(ViewSet):
    @swagger_auto_schema(request_body=CreateSessionSerializer)
    @action(methods=["post"], detail=False)
    def get_session(self, request):
        serializer = CreateSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = create_session(**serializer.validated_data)
        return Response(data={"id": session.id}, status=status.HTTP_303_SEE_OTHER)
