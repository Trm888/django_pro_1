from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание')
    long_description = models.TextField('Полное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    place_id = models.CharField('ID места', max_length=200, unique=True, blank=True, null=True)
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
    image_number = models.IntegerField(validators=[
            MinValueValidator(1)
        ])

    image = models.ImageField()

    def __str__(self):
        return f'{self.image_number} {self.place.title}'

    class Meta:
        verbose_name = 'IMAGE'
        verbose_name_plural = 'IMAGES'