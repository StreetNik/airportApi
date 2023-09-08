from rest_framework import routers

from airplane.views import AirplaneViewSet

router = routers.DefaultRouter()

router.register(r"airplane-list", AirplaneViewSet, basename="airplane-detail")

urlpatterns = [] + router.urls

app_name = "airplane"
