from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from product.models import Category
from product.Serializers.category_Serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # 👈 GET, POST, PUT, DELETE todos públicos

    def get_queryset(self):
        return Category.objects.all().order_by("id")
