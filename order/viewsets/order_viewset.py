from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.Serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
    permission_classes = [AllowAny]
