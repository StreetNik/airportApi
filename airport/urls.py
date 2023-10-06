from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from airport.views import AirportViewSet, CrewViewSet, CrewOccupationViewSet

router = routers.DefaultRouter()

router.register(r"airport-list", AirportViewSet, basename="airport-detail")
router.register(r"crew-list", CrewViewSet, basename="crew-detail")
router.register(r"crew-occupations-list", CrewOccupationViewSet, basename="crew-ocupation-detail")

urlpatterns = [] + router.urls

app_name = "airport"
