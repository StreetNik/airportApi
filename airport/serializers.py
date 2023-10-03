from rest_framework import serializers

from airport.models import Airport, Crew, CrewOccupation


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ["id", "name", "closest_big_city"]


class CrewSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="occupation.name", read_only=True)
    class Meta:
        model = Crew
        fields = ["id", "first_name", "last_name", "occupation", "role", "experience_years"]
        extra_kwargs = {
            "occupation": {"write_only": True},
        }


class CrewOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewOccupation
        fields = ["id", "name"]
