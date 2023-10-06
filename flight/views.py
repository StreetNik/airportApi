from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

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

        queryset = Flight.objects.select_related(
            "route__source",
            "route__destination",
            "airplane"
        ).prefetch_related("tickets")

        if source:
            queryset = queryset.filter(route__source__name__icontains=source)
        if destination:
            queryset = queryset.filter(route__destination__name__icontains=destination)
        if date_range_start:
            queryset = queryset.filter(departure_time__gt=date_range_start)
        if date_range_end:
            queryset = queryset.filter(departure_time__lt=date_range_end)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="source",
                description="Filter flights by source airport name",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name="destination",
                description="Filter flights by destination airport name",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name="date_range_start",
                description="Filter flights in date range starts at this date",
                required=False,
                type=OpenApiTypes.DATE,
            ),
            OpenApiParameter(
                name="date_range_end",
                description="Filter flights in date range ends by this date",
                required=False,
                type=OpenApiTypes.DATE,
            )
        ]
    )
    def list(self, request, *args, **kwargs) -> Response:
        """List of flights with filtering by date, source and destination"""
        return super().list(self, request, *args, **kwargs)


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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="source",
                description="Filter routes by source airport name",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name="destination",
                description="Filter routes by destination airport name",
                required=False,
                type=str
            ),
        ]
    )
    def list(self, request, *args, **kwargs) -> Response:
        """List of routes with filter by name, source and destination"""
        return super().list(self, request, *args, **kwargs)
