from abc import ABC, abstractmethod
from typing import Any, Dict, List
from services.data_source_api import DataSourceAPI
from services.visualizer_api import Visualizer
from model.graph.graph import *

class CoreAPI(ABC):
    @abstractmethod
    def send_data(self, Graph) -> None:
        """Abstract method to send data to Django"""
        pass

    @abstractmethod
    def send_data_tree(self, Graph) -> None:
        """Abstract method to send data to Django"""
        pass

    @abstractmethod
    def get_data(self, params:  Dict[str, Any]):
        """Abstract method to retrieve data from Django"""
        pass
    
    @abstractmethod
    def filter_and_send_data(self, filter_criteria: Dict[str, Any]) -> None:
        """Abstract method to process data, apply filters, and send to Django"""
        pass
    
    @abstractmethod
    def get_plugin_names(self) -> List[str]:
        """Abstarct method that will get installed plugins"""
        pass
    
    @abstractmethod
    def _init_graph(self) -> Graph:
        """Abstract method to initialize a graph"""
        pass

    @abstractmethod
    def get_data_sourcs() -> List[DataSourceAPI]:
        """ Abstract method for getting data source plugins"""
        pass

    @abstractmethod
    def get_visualizers() -> List[Visualizer]:
        """ Abstract method for getting data source plugins"""
        pass
    
    @abstractmethod
    def _filter(self, graph: Graph, filter_criteria: Dict[str, Any]) -> Graph:
        """Abstract method to apply filters to the graph"""
        pass
    
    @abstractmethod
    def _cache_graph(self, graph: Graph):
        """Abstract method that will save current version of the graph"""
        pass

    @abstractmethod
    def send_data(self, graph: str, vizualier:str):
        """Abstract method that will save current version of the graph"""
        pass
