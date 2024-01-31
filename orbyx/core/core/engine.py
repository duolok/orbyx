from typing import Any, Dict, List

import pkg_resources
# from api.graph import Graph
# from api.core_api import CoreAPI
from services.core_api import CoreAPI


def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins

class Engine(CoreAPI):
    # def __init__(self):
    #     self.graph = Graph()
    #
    # def send_data(self, graph):
    #     """Method to send data to Django"""
    #     # Implement sending data logic to Django
    #     pass
    #
    # def get_data(self, query_params: Dict[str, Any]):
    #     """Method to retrieve data from Django"""
    #     # Implement retrieving data logic from Django
    #     pass
    #
    # def filter_and_send_data(self, filter_criteria: Dict[str, Any]):
    #     """Method to process data, apply filters, and send to Django"""
    #     # Implement processing, filtering, and sending data logic
    #     pass
    #
    # def get_plugin_names(self) -> List[str]:
    #     """Method to get installed plugins"""
    #     # Implement getting installed plugins logic
    #     return ["plugin1", "plugin2"]
    #
    # def _init_graph(self):
    #     """Method to initialize a graph"""
    #     # Implement initializing graph logic
    #     self.graph = Graph()
    #
    # def _filter(self, filter_criteria: Dict[str, Any]):
    #     """Method to apply filters to the graph"""
    #     # Implement applying filters to the graph logic
    #     pass
    #
    # def _cache_graph(self):
    #     """Method to save the current version of the graph"""
    #     # Implement caching graph logic
    #     pass
    def send_data(self, graph):
        visualizer = load_plugins("generate_template")
        return visualizer[0].visualize(graph)
