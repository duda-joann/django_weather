
from django.db import models


class City(models.Model):
    """
    Model for all  added to the app cities
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class CityWeather(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    temperature = models.TextField(null=False, blank=False)
    description = models.TextField(max_length = 100, null=False, blank=False)
    icon = models.TextField(max_length=150, null=False, blank=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.city, self.temperature, self.description, self.icon, self.date


