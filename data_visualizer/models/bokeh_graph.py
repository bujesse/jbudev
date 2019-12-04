from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)


class Series(models.Model):
    series_name = models.CharField(max_length=255)
    series_code = models.CharField(max_length=255)


class DataPoint(models.Model):
    year = models.IntegerField(null=True)
    data = models.FloatField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
