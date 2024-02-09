import logging
from typing import Any, Dict, List
from services.core_api import CoreAPI

from services.core_api import Graph

from services.utils import *


from model.graph.graph import Graph
from search.search import SearchProvider
import logging

class Engine(CoreAPI):
    search_provider = None
    def __init__(self):
        self.data_source_plugin = None
        self.visualizer_plugin = None
        self.data_tree = None


    def _set_plugins(self, data_source_plugin: str, visualizer_plugin: str):
        data_source = get_data_source_plugin_by_name(data_source_plugin)
        visualizer = get_visualizer_plugin_by_name(visualizer_plugin)

        if data_source is None or visualizer is None:
            raise ValueError("Invalid data source or visualizer plugin name.")

        self.data_source_plugin = data_source
        self.visualizer_plugin = visualizer

    def send_data(self, data: Any):
        parsed_data = self.data_source_plugin.parse_data(data)  
        graph = self.data_source_plugin.get_graph(parsed_data)
        Engine.search_provider = SearchProvider(graph)
        self.data_tree = graph
        return self.visualizer_plugin.visualize(graph)

    def get_data_sources(self) -> List[DataSourceAPI]:
        return get_data_source_plugins()

    def refresh_view(self):
        graph = Engine.search_provider.sub_graph
        self.data_tree = graph
        visualizer = self.visualizer_plugin
        return visualizer.visualize(graph)

    def send_data_tree(self):
        wikipedia_data_source = self.data_source_plugin
        parsed_data = wikipedia_data_source.parse_data({'project_url' : "D:\\Marko\\Desktop\\iss3\\ISS-Projekat-Tim27\\Nomad Server\\src"})
        graph = wikipedia_data_source.get_graph(parsed_data)
        Engine.search_provider = SearchProvider(graph)

        logging.info("GRAF: ")
        logging.info(graph)
        return graph

    def get_visualizers(self) -> List[Visualizer]:
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

    def _filter(self, filter_criteria: str):
        """Method to apply filters to the graph"""
        return self.search_provider.filter(filter_criteria)
    
    def _search(self, term: str):
        """Method to apply search to the graph"""
        
        return self.search_provider.search(term)
    
    def reset_search(self):
        """Method to reset search parameters"""
        return self.search_provider.reset()
    
    def undo_search(self):
        """Method to reset search parameters"""
        return self.search_provider.undo()


    def _cache_graph(self):
        """Method to save the current version of the graph"""
        # Implement caching graph logic
        pass

