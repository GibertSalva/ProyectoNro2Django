# Generated by Django 2.2 on 2020-07-01 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='producto',
        ),
    ]