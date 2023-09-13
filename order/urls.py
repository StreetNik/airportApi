from rest_framework import routers

from order.views import OrderViewSet, TicketViewSet

router = routers.DefaultRouter()

router.register(r"orders-list", OrderViewSet, basename="airport-detail")
router.register(r"tickets-list", TicketViewSet, basename="ticket-detail")

urlpatterns = [] + router.urls

app_name = "order"
