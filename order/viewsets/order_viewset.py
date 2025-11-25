from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from order.models import Order
from order.Serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        # Visitante → pode acessar GET, mas não deve ver pedidos
        if not user or not user.is_authenticated:
            return Order.objects.none()

        # Usuário autenticado → vê apenas seus pedidos
        return Order.objects.filter(user=user).order_by("id")
