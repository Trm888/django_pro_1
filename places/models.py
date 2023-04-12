from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание')
    long_description = models.TextField('Полное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PLACE'
        verbose_name_plural = 'PLACES'