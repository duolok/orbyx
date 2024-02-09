from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-form-fields/', views.get_form_fields, name='get_form_fields'),
    path('load-graph', views.load_graph, name='load_graph'), 
    path('', views.load_graph_from_plugin, name='index'),
    path('json', views.tree_view_data, name='json'),
    path('refresh', views.filtered_view, name='refresh'),
    path('search/<str:term>', views.search, name='search'),
    path('filter/<str:term>', views.filter, name='search'),
    path('reset', views.reset_search, name='reset'),
    path('undo', views.undo_search, name='reset')
]

