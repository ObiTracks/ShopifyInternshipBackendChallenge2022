# Generated by Django 4.0.4 on 2022-05-22 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_shipment_consignee_shipment_recipient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.shipment'),
        ),
    ]
