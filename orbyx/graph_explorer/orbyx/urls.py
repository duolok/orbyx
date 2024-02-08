from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.load_graph_from_plugin, name='index'),
    path('json', views.tree_view_data, name='json'),
    path('search/<str:term>', views.search, name='search')
]
