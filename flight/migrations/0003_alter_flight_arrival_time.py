# Generated by Django 4.2.5 on 2023-09-10 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0002_alter_flight_options_alter_route_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="arrival_time",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 9, 10, 16, 50, 55, 808942, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
    ]
