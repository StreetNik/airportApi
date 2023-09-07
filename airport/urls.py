from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from airport.views import AirportViewSet

router = routers.DefaultRouter()

router.register(r"airport-list", AirportViewSet, basename="airport-detail")

urlpatterns = [] + router.urls

app_name = "airport"
