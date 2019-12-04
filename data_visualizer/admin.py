from django.contrib import admin

from .models.bokeh_graph import Country, Series

admin.site.register(Country)
admin.site.register(Series)
