# Generated by Django 2.2 on 2020-07-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio', '0004_remove_producto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.BooleanField(max_length=20),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(),
        ),
    ]