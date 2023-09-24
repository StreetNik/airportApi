from rest_framework import serializers
from django.db import transaction

from order.models import Order, Ticket


class TicketSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="get_owner_name", read_only=True)
    flight_name = serializers.CharField(source="flight.__str__", read_only=True)

    class Meta:
        model = Ticket
        fields = ["id", "flight_name", "row", "seat", "flight", "order", "owner_name"]
        extra_kwargs = {
            "flight": {"write_only": True}
        }


class TicketListSerializer(TicketSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "seat", "row", "flight_name"]


class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ["id", "created_at", "user", "username", "tickets"]
        extra_kwargs = {
            "user": {"write_only": True}
        }

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order


class OrderListSerializer(OrderSerializer):
    tickets = TicketListSerializer(many=True, read_only=True)
