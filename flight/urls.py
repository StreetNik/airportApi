from rest_framework import routers

from airport.views import AirportViewSet, CrewViewSet

router = routers.DefaultRouter()

router.register(r"flight-list", AirportViewSet, basename="airport-detail")
router.register(r"route-list", CrewViewSet, basename="crew-detail")

urlpatterns = [] + router.urls

app_name = "flight"