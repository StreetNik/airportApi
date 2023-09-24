from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from order.models import Order, Ticket
from order.serializers import OrderSerializer, TicketSerializer, OrderListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        date_range_start = self.request.query_params.get("date_range_start")
        date_range_end = self.request.query_params.get("date_range_end")

        queryset = Order.objects.all()

        if not user.is_superuser:
            queryset = queryset.filter(user=user)

        if date_range_start:
            queryset = queryset.filter(created_at__gt=date_range_start)
        if date_range_end:
            queryset = queryset.filter(created_at__lt=date_range_end)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
