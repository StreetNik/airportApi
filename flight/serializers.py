from rest_framework import serializers

from flight.models import Route, Flight


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


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ("route", "airplane", "departure_time", "arrival_time")
