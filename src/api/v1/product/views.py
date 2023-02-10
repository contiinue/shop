from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CreateSessionView(ViewSet):
    @action(methods=["post"], detail=False)
    def get_session(self, request):
        return Response(data={"some"})
