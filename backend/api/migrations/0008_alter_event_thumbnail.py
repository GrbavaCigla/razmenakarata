# Generated by Django 4.1.5 on 2023-02-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_event_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="thumbnail",
            field=models.ImageField(upload_to="event/thumbnail"),
        ),
    ]
