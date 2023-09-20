from rest_framework import routers

from flight.views import FlightViewSet, RouteViewSet

router = routers.DefaultRouter()

router.register(r"flight-list", FlightViewSet, basename="airport-detail")
router.register(r"route-list", RouteViewSet, basename="crew-detail")

urlpatterns = [] + router.urls

app_name = "flight"
