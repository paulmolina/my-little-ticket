# Generated by Django 2.0.3 on 2018-04-09 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("tickets", "0005_auto_20180409_1301")]

    operations = [
        migrations.RemoveField(model_name="ticket", name="board"),
        migrations.RemoveField(model_name="ticket", name="score"),
    ]
