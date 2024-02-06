from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_graph_from_plugin, name='index'),
    path('json', views.tree_view_data, name='json')
]
