from rest_framework import serializers
from ..models import store_product

class store_product_Serializer(serializers.ModelSerializer):
    store_name = serializers.CharField(source='store.name', read_only=True)
    product_name = serializers.CharField(source='product.product_type', read_only=True)
    class Meta:
        model = store_product
        fields = ['store_name', 'product_name', 'price']
