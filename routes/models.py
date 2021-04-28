from cities.models import City

from django.db import models
from django.urls import reverse   # Noqa

from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Routes name')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Total travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_from_city_set',
                                  verbose_name='from city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                related_name='route_to_city_set',
                                verbose_name='In city')
    trains = models.ManyToManyField(Train, verbose_name='Through cities')

    def __str__(self):
        return f'Routes {self.name}| from {self.from_city} to {self.to_city}'

    # def get_absolute_url(self):
    #     return reverse('trains:train-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['name']
