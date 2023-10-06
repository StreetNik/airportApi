from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from order.models import Order
from order.serializers import OrderSerializer, OrderListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        username = self.request.query_params.get("username")
        date_range_start = self.request.query_params.get("date_range_start")
        date_range_end = self.request.query_params.get("date_range_end")

        queryset = Order.objects.select_related("user").prefetch_related(
            "tickets__flight__route__source",
            "tickets__flight__route__destination",
        )

        if date_range_start:
            queryset = queryset.filter(created_at__gt=date_range_start)
        if date_range_end:
            queryset = queryset.filter(created_at__lt=date_range_end)
        if not user.is_superuser:
            queryset = queryset.filter(user=user)
            return queryset

        if username:
            user = User.objects.get(username=username)
            queryset = queryset.filter(user=user)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="username",
                description="Filter orders by username(Superusers only)",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name="date_range_start",
                description="Filter orders in date range starts at this date",
                required=False,
                type=OpenApiTypes.DATE,
            ),
            OpenApiParameter(
                name="date_range_end",
                description="Filter orders in date range ends by this date",
                required=False,
                type=OpenApiTypes.DATE,
            )
        ]
    )
    def list(self, request, *args, **kwargs) -> Response:
        """List of orders with filtering by date and username"""
        return super().list(self, request, *args, **kwargs)
