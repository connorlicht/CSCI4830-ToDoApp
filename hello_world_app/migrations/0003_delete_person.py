# Generated by Django 5.1.6 on 2025-03-19 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world_app', '0002_todoevent_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
