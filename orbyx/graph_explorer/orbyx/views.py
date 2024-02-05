import os
import sys
import xml.etree.ElementTree as ET
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

import pkg_resources

def index(request):
    template = loader.get_template('orbyx/index.html')
    return HttpResponse(template.render({}, request))

def get_data_source_plugins():
    return [ep.load() for ep in pkg_resources.iter_entry_points(group='orbyx_data_source_plugin')]

def get_visualizer_plugins():
    return [ep.load() for ep in pkg_resources.iter_entry_points(group='orbyx_visualizer_plugin')]

def get_engine():
    return next(pkg_resources.iter_entry_points('core')).load()

'''This will be replaced once action for applying data source and visualization are implemented.'''
def load_graph_from_plugin(request):
    data_sources = get_data_source_plugins()
    visualizers = get_visualizer_plugins()
    engine = get_engine()

    visualization = engine.send_data(None, "AYO")
    template = loader.get_template('orbyx/index.html')
    return HttpResponse(template.render({'main_view': mark_safe(visualization)}, request))