import logging
from typing import Any, Dict, List
from services.core_api import CoreAPI
from services.utils import *
import pkg_resources

class Engine(CoreAPI):
    def __init__(self):
        self.data_source_plugin = None
        self.visualizer_plugin = None
        self.data_tree = None

    def _set_plugins(data_source_plugin, visualizer_plugin):
        self.data_source_plugin = data_source_plugin
        self.visualizer_plugin = visualizer_plugin

    def send_data(self, graph):
        wikipedia_data_source = get_data_source_plugin_by_name("Tinywiki")
        parsed_data = wikipedia_data_source.parse_data("some link will be here")  
        graph = wikipedia_data_source.get_graph(parsed_data)
        self.data_tree = graph
        visualizer = get_visualizer_plugin_by_name("Simple Visualizer")
        return visualizer.visualize(graph)

    def send_data_tree(self):
        wikipedia_data_source = get_data_source_plugin_by_name("Tinywiki")
        parsed_data = wikipedia_data_source.parse_data("some link will be here")
        graph = wikipedia_data_source.get_graph(parsed_data)
        logging.info("GRAF: ")
        logging.info(graph)
        return graph

    def get_data_sources() -> List[DataSourceAPI]:
        return get_data_source_plugins()

    def get_visualizers() -> List[Visualizer]:
        return get_visualizer_plugins()


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

