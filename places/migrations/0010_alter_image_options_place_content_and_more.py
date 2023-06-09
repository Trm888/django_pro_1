# Generated by Django 4.2 on 2023-04-13 11:19

import django.core.validators
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_image_image_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_number', 'place'], 'verbose_name': 'IMAGE', 'verbose_name_plural': 'IMAGES'},
        ),
        migrations.AddField(
            model_name='place',
            name='content',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
