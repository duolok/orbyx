from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-form-fields/', views.get_form_fields, name='get_form_fields'),
    path('load-graph', views.load_graph, name='load_graph'), 
]

