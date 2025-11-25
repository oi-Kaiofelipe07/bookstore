from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.Serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")

    def get_permissions(self):
        # Somente métodos destrutivos exigem autenticação
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated()]

        # GET e POST são públicos (os testes exigem isso)
        return [AllowAny()]
