from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import store
from ..serializers import storeSerializer



class StoreView(APIView):
    model = store
    serializer = storeSerializer

    def post(self, request, *args, **kwargs):
        try:
            store_serializered = self.serializer(data=request.data)
            if store_serializered.is_valid():
                store_serializered.save()
                return Response(status=status.HTTP_201_CREATED, data= store_serializered.data)
            store = self.model.objects.get(address=request.data['address'])
            response = {
                'error':'store exits in this address',
                'id' : store.id
            }
            return Response(status=status.HTTP_400_BAD_REQUEST, data= response)
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= error)