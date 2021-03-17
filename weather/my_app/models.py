from django.db import models


class City(models.Model):
    choices = [
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Australia/Oceania', 'Australia/Oceania'),
        ('Antarctica', 'Antarctica')]

    name = models.CharField(max_length=25)
    continent = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
