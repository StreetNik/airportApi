# Generated by Django 4.2.5 on 2023-09-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0003_alter_flight_arrival_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="route",
            name="distance",
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
