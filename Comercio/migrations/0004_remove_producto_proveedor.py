# Generated by Django 2.2 on 2020-07-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio', '0003_auto_20200701_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
    ]
