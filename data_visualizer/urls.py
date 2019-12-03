from django.urls import path

from data_visualizer.views import index, bokeh_graph

urlpatterns = [
    path('', index.index, name='index'),
    path('bokeh_graph/', bokeh_graph.bokeh_graph, name='bokeh_graph'),
    path('bokeh_graph/get_graph', bokeh_graph.get_bokeh_graph, name='bokeh_graph_get_graph'),
]
