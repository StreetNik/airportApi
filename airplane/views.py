from rest_framework.viewsets import ModelViewSet

from airplane.models import Airplane, AirplaneType
from airplane.serializers import AirplaneSerializer, AirplaneTypeSerializer


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneTypeViewSet(ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
