from rest_framework.viewsets import ModelViewSet

from airport.models import Airport, Crew
from airport.serializers import AirportSerializer, CrewSerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
