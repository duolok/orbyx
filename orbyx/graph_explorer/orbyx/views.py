import os
import sys
import xml.etree.ElementTree as ET
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context
import pkg_resources


def get_engine():
    return next(pkg_resources.iter_entry_points('core')).load()

def index(request):
    data_sources = get_data_source_plugins()
    visualizers = get_visualizer_plugins()

    print("Data Sources:", data_sources)
    print("Visualizers:", visualizers)

    context = {
        'data_sources': data_sources,
        'visualizers': visualizers,
    }

    return render(request, 'orbyx/index.html', context)

def load_graph_from_plugin(request):
    engine = get_engine()
    data_sources = engine.get_data_sources()
    visualizers = engine.get_visualizers()

    visualization = engine.send_data(None, "Example Visualization Data")
    
    context = {
        'main_view': mark_safe(visualization), 
        'data_sources': data_sources,
        'visualizers': visualizers,
    }
    
    return render(request, 'orbyx/index.html', context)
