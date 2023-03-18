
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound

from ..models import product
from ..serializers import productSerializer

class ProductView(APIView):
    model = product
    serializer = productSerializer
    lookup_field = 'branch'

    def put(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.get(branch=kwargs['branch'])
        except self.model.DoesNotExist:
            raise NotFound('Prduct not found')
        try:
            product_serialized = self.serializer(instance, data=request.data)
            product_serialized.is_valid(raise_exception=True)
            product_serialized.save()
            return Response(status=status.HTTP_200_OK, data=product_serialized.data)
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= str(error))


    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data='Product created')
            return Response(status=status.HTTP_400_BAD_REQUEST, data= serializer.errors)
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= error)