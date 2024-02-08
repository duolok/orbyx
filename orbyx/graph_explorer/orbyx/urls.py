from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_graph_from_plugin, name='index'),
    path('add_workspace/', views.add_workspace, name='add_workspace')
]
