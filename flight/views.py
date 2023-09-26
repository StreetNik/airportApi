from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from AirportAPI.permissions import IsSuperuserOrReadOnly
from flight.models import Flight, Route
from flight.serializers import RouteSerializer, FlightSerializer


class FlightViewSet(ModelViewSet):
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = FlightSerializer

    def get_queryset(self):
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        date_range_start = self.request.query_params.get("date_range_start")
        date_range_end = self.request.query_params.get("date_range_end")

        queryset = Flight.objects.all().select_related("route__source", "route__destination", "airplane")
        queryset = queryset.prefetch_related("tickets")

        if source:
            queryset = queryset.filter(route__source__name__icontains=source)
        if destination:
            queryset = queryset.filter(route__destination__name__icontains=destination)
        if date_range_start:
            queryset = queryset.filter(departure_time__gt=date_range_start)
        if date_range_end:
            queryset = queryset.filter(departure_time__lt=date_range_end)

        return queryset


class RouteViewSet(ModelViewSet):
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = RouteSerializer

    def get_queryset(self):
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")

        queryset = Route.objects.all()

        if source:
            queryset = queryset.filter(source__name__icontains=source)
        if destination:
            queryset = queryset.filter(destination__name__icontains=destination)

        return queryset
