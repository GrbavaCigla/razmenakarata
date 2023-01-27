# Generated by Django 4.1.5 on 2023-01-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]