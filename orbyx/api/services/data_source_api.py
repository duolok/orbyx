from abc import ABC, abstractmethod
from typing import Any, Dict, List
from model.graph.graph import Graph
class DataSourceAPI(ABC):
    # @abstractmethod
    def get_name(self) -> str:
        """Abstract property for the name of the data source"""
        pass

    @abstractmethod
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        """Method that will parse data and consturct a graph"""
        pass

    @abstractmethod
    def get_graph(self, parsed_data: List[Dict[str, Any]]) -> Graph:
        """Method that will send data to the plugin and recieve a graph"""
        pass
