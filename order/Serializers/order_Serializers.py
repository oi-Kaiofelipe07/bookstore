from rest_framework import serializers

from product.models.product import Product
from product.Serializers.product_Serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Product
        fields = ['product', 'total']