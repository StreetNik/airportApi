from rest_framework.viewsets import ModelViewSet

from order.models import Order, Ticket
from order.serializers import OrderSerializer, TicketSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
