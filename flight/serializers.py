from rest_framework import serializers

from flight.models import Route, Flight
from order.models import Ticket


class RouteSerializer(serializers.ModelSerializer):
    source_airport_name = serializers.SerializerMethodField()
    destination_airport_name = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = ("source_airport_name", "destination_airport_name", "distance", "source", "destination")
        read_only_fields = ("source_airport_name", "destination_airport_name")
        extra_kwargs = {"source": {"write_only": True}, "destination": {"write_only": True}}

    def get_source_airport_name(self, obj):
        return obj.source.name

    def get_destination_airport_name(self, obj):
        return obj.destination.name


class TicketSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("row", "seat",)


class FlightSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True, source="airplane.capacity")
    taken_seats = TicketSeatsSerializer(many=True, source="tickets", read_only=True)

    class Meta:
        model = Flight
        fields = ("route", "airplane", "departure_time", "arrival_time", "capacity", "taken_seats")
