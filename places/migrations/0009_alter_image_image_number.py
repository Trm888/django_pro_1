# Generated by Django 4.2 on 2023-04-13 03:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_image_image_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
