from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=255)
    closest_big_city = models.CharField(max_length=255)

    class Meta:
        ordering = ("closest_big_city",)

    def __str__(self):
        return self.name + " - " + self.closest_big_city


class CrewOccupation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    occupation = models.ForeignKey(CrewOccupation, on_delete=models.CASCADE)
    experience_years = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    class Meta:
        ordering = ("first_name", "last_name",)

    def __str__(self):
        return self.first_name + " " + self.last_name + self.occupation.name
