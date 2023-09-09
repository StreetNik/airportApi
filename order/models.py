from django.db import models
from django.contrib.auth import get_user_model

from flight.models import Flight


class Order(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField
    seat = models.IntegerField
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.flight
