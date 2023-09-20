from django.db import models

from django.core.exceptions import ValidationError
from django.utils import timezone

from airplane.models import Airplane
from airport.models import Airport


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="source_routes")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination_routes")
    distance = models.IntegerField()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.source.name} - {self.destination.name}"

    def clean(self):
        if self.source == self.destination:
            raise ValidationError("Source and destination airports cannot be the same.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    class Meta:
        ordering = ("-departure_time",)

    def __str__(self):
        return f"{self.route.source.name} - {self.route.destination.name}, {self.departure_time}"

    def clean(self):
        if self.departure_time >= self.arrival_time:
            raise ValidationError("Arrival time cannot be later then departure time.")
        if self.departure_time < timezone.now():
            raise ValidationError("Departure time cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
