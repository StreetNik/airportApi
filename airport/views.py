from rest_framework.viewsets import ModelViewSet

from airport.models import Airport
from airport.serializers import AirportSerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
