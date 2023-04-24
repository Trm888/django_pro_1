from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    short_description = models.TextField('Краткое описание', blank=True)
    lat = models.FloatField('Широта', null=True)
    lon = models.FloatField('Долгота', null=True)
    place_id = models.CharField('ID места', max_length=200, unique=True, blank=True, null=True)
    long_description = HTMLField('Полное описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PLACE'
        verbose_name_plural = 'PLACES'


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
        verbose_name = 'IMAGE'
        verbose_name_plural = 'IMAGES'
        ordering = ['image_number', 'place']
        unique_together = ['id', 'place', 'image']
