from rest_framework import serializers

from order.models import Order, Ticket


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="username"
    )

    class Meta:
        model = Order
        fields = ["id", "created_at", "user"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "flight", "order"]
