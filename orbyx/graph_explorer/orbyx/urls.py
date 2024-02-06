from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.load_graph_from_plugin, name='index')
    # path('simple/', views.load_graph_simple, name='simple'),
    # path('block/', views.load_graph_block, name='block')
]
