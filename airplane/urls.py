from rest_framework import routers

from airplane.views import AirplaneViewSet, AirplaneTypeViewSet

router = routers.DefaultRouter()

router.register(r"airplane-list", AirplaneViewSet, basename="airplane-detail")
router.register(r"airplane-type-list", AirplaneTypeViewSet, basename="airplane-type-detail")

urlpatterns = [] + router.urls

app_name = "airplane"
