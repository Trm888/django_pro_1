from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    short_description = models.TextField('Краткое описание', blank=True)
    lat = models.FloatField('Широта', null=True)
    lon = models.FloatField('Долгота', null=True)
    long_description = HTMLField('Полное описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'МЕСТО'
        verbose_name_plural = 'МЕСТА'


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    image_number = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])

    image = models.ImageField(unique=True)

    def __str__(self):
        return f'{self.image_number} {self.place.title}'

    class Meta:
        verbose_name = 'КАРТНКА'
        verbose_name_plural = 'КАРТИНКИ'
        ordering = ['image_number', 'place']
        unique_together = ['id', 'place', 'image']
