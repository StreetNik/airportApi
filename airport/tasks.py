from celery import Celery
from airport.models import Crew

from decimal import Decimal


celery = Celery("AirportAPI")


@celery.task
def monthly_crew_exp_update():
    crew_queryset = Crew.objects.all()
    print("Works")

    for crew_member in crew_queryset:
        crew_member.experience_years += Decimal("0.12")
        crew_member.save()
