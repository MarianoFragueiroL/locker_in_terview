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
        try:
            product_price = request.data.pop('price')
            store_name = request.data.pop('store')
            product_name = request.data.pop('product')
            product = (self.product_model.objects.get(
            **product_name, 
                ))
        except Exception as error:
            return Response(status=status.HTTP_409_CONFLICT, data= 'Product Doesnt exits')
        try:
            store = self.store_model.objects.get(**store_name)
        except Exception as error:
            return Response(status=status.HTTP_409_CONFLICT, data= 'Store Doesnt exits')

        try:
            store_product =  self.model.objects.get(
                store = store,
                product = product
            )
        except self.model.DoesNotExist:
                store_product = None
        if store_product is not None:
            store_product.price = product_price
            store_product.save()
            return Response(status=status.HTTP_200_OK, data='price updated')
        try:
            new_price = self.model.objects.create(
                price = product_price,
                store = store,
                product = product
            )
            if new_price.id:
                return Response(status=status.HTTP_201_CREATED, data='price for product added')
            else:
                return Response(status=status.HTTP_409_CONFLICT, data='Error saving the price for product')

        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= str(error))

