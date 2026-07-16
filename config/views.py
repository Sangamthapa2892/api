from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class BaseApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
