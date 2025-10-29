from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.Serializers.product_Serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")