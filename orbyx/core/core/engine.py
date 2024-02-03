from typing import Any, Dict, List
from api.services.core_api import CoreAPI
from api.services.core_api import Graph
import pkg_resources

''' This method will be removed once plugin pipeline is implemented. '''
def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins

class Engine(CoreAPI):
    def __init__(self):
        self.data_source_plugin = None
        self.visualizer_plugin = None

    def _set_plugins(self, data_source_plugin, visualizer_plugin):
        self.data_source_plugin = data_source_plugin
        self.visualizer_plugin = visualizer_plugin

    def send_data(self, graph):
        visualizer = load_plugins("generate_template")
        return visualizer[0].visualize(graph)

    def get_data(self, query_params: Dict[str, Any]):
        """Method to retrieve data from Django"""
        # Implement retrieving data logic from Django
        pass

    def filter_and_send_data(self, filter_criteria: Dict[str, Any]):
        """Method to process data, apply filters, and send to Django"""
        # Implement processing, filtering, and sending data logic
        pass

    def get_plugin_names(self) -> List[str]:
        """Method to get installed plugins"""
        # Implement getting installed plugins logic
        return ["plugin1", "plugin2"]

    def _init_graph(self):
        """Method to initialize a graph"""
        # Implement initializing graph logic
        self.graph = Graph()

    def _filter(self, filter_criteria: Dict[str, Any]):
        """Method to apply filters to the graph"""
        # Implement applying filters to the graph logic
        pass

    def _cache_graph(self):
        """Method to save the current version of the graph"""
        # Implement caching graph logic
        pass

