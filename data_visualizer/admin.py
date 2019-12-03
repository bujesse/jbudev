from django.contrib import admin

from .models.bokeh_graph import CountryData, YearlyData

admin.site.register(CountryData)
admin.site.register(YearlyData)
