# Generated by Django 3.0.5 on 2020-04-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_eventstobaby'),
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='babie',
            name='eventsToBaby',
            field=models.ManyToManyField(to='events.Event'),
        ),
    ]
