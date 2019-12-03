from djongo import models


class YearlyData(models.Model):
    year = models.IntegerField()
    data = models.FloatField()


class CountryData(models.Model):
    series_name = models.CharField(max_length=255)
    series_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    yearly_data = models.ArrayModelField(
        model_container=YearlyData,
    )

    objects = models.DjongoManager()
