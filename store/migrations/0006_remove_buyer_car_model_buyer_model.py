# Generated by Django 5.0.1 on 2024-02-20 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_car_model_buyer_car_model_alter_car_car_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='car_model',
        ),
        migrations.AddField(
            model_name='buyer',
            name='model',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.car_model'),
            preserve_default=False,
        ),
    ]
