from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import store
from ..serializers import storeSerializer



class StoreView(APIView):
    model = store
    serializer = storeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data='Store created')
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= error)