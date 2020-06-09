from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Home(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        return Response('Ok', status=200)
