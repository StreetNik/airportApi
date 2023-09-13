from rest_framework.viewsets import ModelViewSet

from order.models import Order, Ticket
from order.serializers import OrderSerializer, TicketSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
