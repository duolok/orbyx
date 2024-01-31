# from core.proba import IspisCore
import xml.etree.ElementTree as ET

from django.utils.safestring import mark_safe
from services.core_api import CoreAPI
import pkg_resources
import services.core_api
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context


def index(request):
    template = loader.get_template('orbyx/index.html')
    return HttpResponse(template.render({}, request))


def load_plugins():
    plugins = []
    for ep in pkg_resources.iter_entry_points(group="django_app"):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins


def load_graph_from_plugin(request):
    plugins = load_plugins()
    template = loader.get_template('orbyx/index.html')
    return HttpResponse(template.render({'main_view': mark_safe(plugins[0].send_data("parsed_graph_data"))}))


