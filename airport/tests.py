from .tasks import monthly_crew_exp_update
from datetime import datetime, timedelta
import subprocess
from .models import CrewOccupation, Crew
from decimal import Decimal
from celery.contrib.testing.worker import start_worker
from django.test import SimpleTestCase
from AirportAPI.celery import app
from mock import Mock, patch

import time


class MonthlyCrewExpUpdate(SimpleTestCase):
    databases = '__all__'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Start up celery worker
        cls.celery_worker = start_worker(app, perform_ping_check=False)
        cls.celery_worker.__enter__()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Close worker
        cls.celery_worker.__exit__(None, None, None)

    def test_task_add_exp_as_expected(self):
        crew_occupation = CrewOccupation.objects.create(name="Pilot")
        crew = Crew.objects.create(
            first_name="Test",
            last_name="Test",
            occupation=crew_occupation,
            experience_years=0
        )
        crew.save()

        res = monthly_crew_exp_update.delay()
        res.get()

        res_crew = Crew.objects.get(id=crew.id)

        self.assertEqual(res_crew.experience_years, Decimal("0.12"))

    def test_task_is_called_every_month(self):
        # Create a mock object for the task.
        mock_task = Mock()

        for crew in Crew.objects.all():
            print(crew.experience_years)

        # Patch the task with the mock object.
        with patch("airport.tasks.monthly_crew_exp_update", mock_task):
            celery_beat_process = subprocess.Popen(
                [
                    "celery", "-A", "AirportAPI", "beat", "--loglevel", "INFO",
                    "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler"
                ]
            )

            # celery_beat_process.wait(timeout=10)
            time.sleep(10)
            current_time = datetime(2023, 10, 1)

            current_time += timedelta(days=31)

            celery_beat_process.terminate()

            for crew in Crew.objects.all():
                print(crew.experience_years)
            self.assertEqual(mock_task.call_count, 2)
