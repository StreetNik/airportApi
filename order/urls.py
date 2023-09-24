from rest_framework import routers

from order.views import OrderViewSet

router = routers.DefaultRouter()

router.register(r"orders-list", OrderViewSet, basename="airport-detail")

urlpatterns = [] + router.urls

app_name = "order"
