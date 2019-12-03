from django.shortcuts import render
from django.http import Http404
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Turbo11 as palette
from bokeh.embed import components
from data_visualizer.models import CountryData
from helpers import db_helpers


def bokeh_graph(request):
    all_series = list(db_helpers.get_distinct(CountryData, ['series_name', 'series_code']))
    all_series.sort(key=lambda x: x['series_name'])

    all_countries = list(db_helpers.get_distinct(CountryData, ['country_name', 'country_code']))
    all_countries.sort(key=lambda x: x['country_name'])

    return render(request, 'data_visualizer/bokeh_graph.html', {'all_series': all_series, 'all_countries': all_countries})


def get_bokeh_graph(request):
    series_code = request.GET.get('series_code')
    country_codes = request.GET.getlist('countries')

    country_data = CountryData.objects.filter(series_code=series_code, country_code__in=country_codes).all()
    if not country_data:
        raise Http404("Code and series does not exist")

    plot = figure(title='Line Graph', x_axis_label='Year', y_axis_label=country_data[0].series_name, plot_width=1200, plot_height=600)

    for i, entry in enumerate(country_data[:10]):
        data = []
        year = []
        for yearly_data in entry.yearly_data:
            year.append(yearly_data.year)
            data.append(yearly_data.data)
        plot.line(year, data, legend_label=entry.country_code, line_color=palette[i])

    script, div = components(plot)
    return render(request, 'data_visualizer/line_graph.html', {'script': script, 'div': div})
