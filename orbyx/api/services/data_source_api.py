from abc import ABC, abstractmethod
from typing import Any, Dict, List
from api.services.core_api import Graph
class DataSourceAPI(ABC):
    @abstractmethod
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        """Method that will parse data and consturct a graph"""
        pass

    @abstractmethod
    def get_data(self) -> Graph:
        """Method that will send data to the plugin and recieve a graph"""
        pass
