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


    def get(self, request, *args, **kwargs):
        try:
            # query = request.POST.dict()
            store = self.store_model.objects.get(name= kwargs['name'])
            filters = {
                'store': store,
            }

            store_product = (self.model.objects
                        .filter(**filters)
                        )
            store_product_serialized = self.serializer(store_product, many=True)
            return Response(status=status.HTTP_200_OK, data=store_product_serialized.data)
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= str(error))

    def post(self, request, *args, **kwargs):
        product_price = request.data.pop('price')
        store_name = request.data.pop('store')
        product_name = request.data.pop('product')
        product = (self.product_model.objects.filter(
           **product_name
            ))[0]
        store = self.store_model.objects.filter(**store_name)
        store_product =  self.model.objects.get(
            store = store,
            product = product
        )
        if store_product.exists() >0:
            store_product.price = product_price
            store_product.save()
            return Response(status=status.HTTP_201_CREATED, data='price updated')

        try:
            self.model.objects.create(
                price = product_price,
                store = store,
                product = product
            )
            return Response(status=status.HTTP_201_CREATED, data='price for product added')
        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= str(error))

