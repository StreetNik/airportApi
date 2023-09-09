from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from flight.models import Flight


class Order(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        ordering = ("order",)
        unique_together = ("row", "seat", "flight")

    def clean(self):
        if self.row < 1 or self.row > self.flight.airplane.rows:
            raise ValidationError("Row number is not within the valid range for this plane.")
        if self.seat < 1 or self.seat > self.flight.airplane.seats_in_row:
            raise ValidationError("Seat number is not within the valid range for this plane.")

    def __str__(self):
        return self.flight
