from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from AirportAPI.permissions import IsSuperuserOrReadOnly
from airplane.models import Airplane, AirplaneType
from airplane.serializers import AirplaneSerializer, AirplaneTypeSerializer


class AirplaneViewSet(ModelViewSet):
    serializer_class = AirplaneSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        name = self.request.query_params.get("name")
        type = self.request.query_params.get("type")

        queryset = Airplane.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        if type:
            queryset = queryset.filter(airplane_type__name=type)

        return queryset.distinct()


class AirplaneTypeViewSet(ModelViewSet):
    serializer_class = AirplaneTypeSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        name = self.request.query_params.get("name")

        queryset = AirplaneType.objects.all()

        if name:
            queryset = queryset.filter(name=name)

        return queryset

