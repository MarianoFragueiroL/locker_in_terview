from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import AUTOBotApp

# Create your views here.
class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        content = { 'message': 'Hello, World!'}
        return Response(content)