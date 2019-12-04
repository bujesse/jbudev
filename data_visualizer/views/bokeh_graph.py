from django.shortcuts import render
from django.http import Http404
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Turbo11 as palette
from bokeh.embed import components
from data_visualizer.models import Country, Series, DataPoint


def bokeh_graph(request):
    all_series = list(Series.objects.order_by('series_name').all())
    all_countries = list(Country.objects.order_by('country_name').all())

    return render(request, 'data_visualizer/bokeh_graph.html', {'all_series': all_series, 'all_countries': all_countries})


def get_bokeh_graph(request):
    series_code = request.GET.get('series_code')
    country_codes = request.GET.getlist('countries')

    series = Series.objects.get(series_code=series_code)
    countries = Country.objects.filter(country_code__in=country_codes)

    plot = figure(title='Line Graph', x_axis_label='Year', y_axis_label=series.series_name, plot_width=1200, plot_height=600)

    for i, country in enumerate(countries):
        data_points = DataPoint.objects.filter(series=series, country=country).all()
        if not data_points:
            raise Http404("Code and series does not exist")

        data = []
        year = []
        for entry in data_points:
            year.append(entry.year)
            data.append(entry.data)
        plot.line(year, data, legend_label=country.country_code, line_color=palette[i])

    script, div = components(plot)
    return render(request, 'data_visualizer/line_graph.html', {'script': script, 'div': div})
