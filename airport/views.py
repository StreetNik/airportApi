from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from AirportAPI.permissions import IsSuperuserOrReadOnly
from airport.models import Airport, Crew
from airport.serializers import AirportSerializer, CrewSerializer


class AirportViewSet(ModelViewSet):
    serializer_class = AirportSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        name = self.request.query_params.get("name")
        city = self.request.query_params.get("city")

        queryset = Airport.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        if city:
            queryset = queryset.filter(closest_big_city__icontains=city)

        return queryset


class CrewViewSet(ModelViewSet):
    serializer_class = CrewSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        first_name = self.request.query_params.get("first_name")
        last_name = self.request.query_params.get("last_name")

        queryset = Crew.objects.all()

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset
