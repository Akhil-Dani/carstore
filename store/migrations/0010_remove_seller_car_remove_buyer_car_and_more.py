# Generated by Django 5.0.1 on 2024-02-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_brand_car_model_model_car_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='car',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='car',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='model',
        ),
        migrations.AddField(
            model_name='car',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='first_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=55),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
