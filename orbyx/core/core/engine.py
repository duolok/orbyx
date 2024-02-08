from typing import Any, Dict, List
from services.core_api import CoreAPI
from services.utils import *
import pkg_resources

class Engine(CoreAPI):
    def __init__(self):
        self.data_source_plugin = None
        self.visualizer_plugin = None

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
        return self.visualizer_plugin.visualize(graph)

    def get_data_sources(self) -> List[DataSourceAPI]:
        return get_data_source_plugins()

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

    def _filter(self, filter_criteria: Dict[str, Any]):
        """Method to apply filters to the graph"""
        # Implement applying filters to the graph logic
        pass

    def _cache_graph(self):
        """Method to save the current version of the graph"""
        # Implement caching graph logic
        pass

