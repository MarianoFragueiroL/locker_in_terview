from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import store_product, store ,product
from .  .serializers import store_product_Serializer



class Product_Store_View(APIView):
    model = store_product
    serializer = store_product_Serializer
    product_model = product
    store_model = store




    def post(self, request, *args, **kwargs):

        product = self.product_model.objects.get(branch=request.data['product']['branch'])
        store = self.store_model.objects.get(name=request.data['store']['name'])
        data = {
            'price' : request.data['price'],
            'store' : store,
            'product' : product
        }
        try:
            self.model.objects.get_or_create(data)
            return Response(status=status.HTTP_201_CREATED, data='price for product added')
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= error)

