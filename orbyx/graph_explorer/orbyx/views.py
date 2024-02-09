import logging
import os
import sys
import threading
import xml.etree.ElementTree as ET
from django.utils.safestring import mark_safe
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import pkg_resources

class EngineSingleton:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                engine_class = next(pkg_resources.iter_entry_points('core')).load()
                cls._instance = engine_class()
        return cls._instance

def get_engine():
    return EngineSingleton.get_instance()

def index(request):
    engine = get_engine()  
    data_sources = engine.get_data_sources()
    visualizers = engine.get_visualizers()

    context = {
        'data_sources': data_sources,
        'visualizers': visualizers,
    }
    return render(request, 'orbyx/index.html', context)

def get_form_fields(request):
    data_source = request.GET.get('data_source')
    visualizer = request.GET.get('visualizer')
    if not data_source or not visualizer:
        return JsonResponse({'error': 'Missing or invalid data_source or visualizer parameters'}, status=400)
    engine = get_engine()  
    try:
        engine._set_plugins(data_source, visualizer)
        fields = engine.data_source_plugin.get_requirements()
        return JsonResponse({'fields': fields})
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def load_graph(request):
    engine = get_engine()
    data_sources = engine.get_data_sources()
    visualizers = engine.get_visualizers()
    visualization = engine.send_data(json.loads(request.body))

    context = {
        'main_view': mark_safe(visualization), 
        'data_sources': data_sources,
        'visualizers': visualizers,
    }

    return render(request, 'orbyx/index.html', context) 
    
def tree_view_data(request: HttpRequest):
    engine = get_engine()
    graph = engine.data_tree
    nodes = graph.serialize_nodes()
    edges = graph.serialize_edges()

    return JsonResponse({'nodes': nodes, 'edges':edges})


def search(request: HttpRequest, term):
    engine = get_engine()
    
    graph = engine._search(term)

    nodes = graph.serialize_nodes()
    edges = graph.serialize_edges()
  
    return JsonResponse({'nodes': nodes, 'edges':edges})
  
def filtered_view(request: HttpRequest):
    engine = get_engine()
    
    visualization = engine.refresh_view()
    
    return JsonResponse({"visualization": mark_safe(visualization)})

def reset_search(request: HttpRequest):
    engine = get_engine()
    graph = engine.reset_search()

    nodes = graph.serialize_nodes()
    edges = graph.serialize_edges()

    return JsonResponse({'nodes': nodes, 'edges':edges})

def undo_search(reuest: HttpRequest):
    engine = get_engine()
    graph = engine.undo_search()

    nodes = graph.serialize_nodes()
    edges = graph.serialize_edges()

    return JsonResponse({'nodes': nodes, 'edges':edges})

def filter(request: HttpRequest, term: str):
   
    engine = get_engine()
    graph = engine._filter(term)

    nodes = graph.serialize_nodes()
    edges = graph.serialize_edges()
    return JsonResponse({'nodes': nodes, 'edges':edges})


