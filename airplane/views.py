from rest_framework.viewsets import ModelViewSet

from airplane.models import Airplane
from airplane.serializers import AirplaneSerializer


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
