from rest_framework import serializers

from flight.models import Route, Flight
from order.models import Ticket


class RouteSerializer(serializers.ModelSerializer):
    source_airport_name = serializers.SerializerMethodField()
    destination_airport_name = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = (
            "id", "source_airport_name",
            "destination_airport_name", "distance",
            "source", "destination"
        )
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
    route_name = serializers.CharField(source="route.__str__", read_only=True)
    airplane_name = serializers.CharField(source="airplane.__str__", read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id", "route_name", "airplane_name",
            "departure_time", "arrival_time", "capacity",
            "taken_seats", "route", "airplane"
        )
        read_only_fields = ("route_name", "airplane_name")
        extra_kwargs = {
            "route": {"write_only": True},
            "airplane": {"write_only": True}
        }
