from celery import Celery
from airport.models import Crew

from decimal import Decimal


celery = Celery("AirportAPI", backend="redis", broker="redis://localhost/")


@celery.task
def monthly_crew_exp_update():
    crew_queryset = Crew.objects.all()

    for crew_member in crew_queryset:
        crew_member.experience_years += Decimal("0.12")
        crew_member.save()
