from rest_framework import serializers

from airplane.models import Airplane, AirplaneType


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ["id", "name"]


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type_name = serializers.CharField(source="airplane_type.name", read_only=True)

    class Meta:
        model = Airplane
        fields = [
            "id", "name", "rows",
            "seats_in_row", "airplane_type",
            "airplane_type_name"
        ]
        extra_kwargs = {"airplane_type": {"write_only": True}}
