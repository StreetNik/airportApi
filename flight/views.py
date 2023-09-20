from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from AirportAPI.permissions import IsSuperuserOrReadOnly
from flight.models import Flight, Route
from flight.serializers import RouteSerializer, FlightSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()

    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = FlightSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()

    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = RouteSerializer
