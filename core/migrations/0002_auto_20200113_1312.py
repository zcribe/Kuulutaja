# Generated by Django 3.0.1 on 2020-01-13 13:12

from django.db import migrations
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        HStoreExtension(),
    ]
