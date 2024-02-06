from abc import ABC, abstractmethod
from typing import Any

from model.graph.graph import Graph


class Visualizer(ABC):
    @abstractmethod
    def get_name(self) -> str:
        """Abstract property for the name of the visualizer"""
        pass

    @abstractmethod
    def visualize(self, graph: Graph) -> Any:
        """Abstract method for data visualization"""
        pass
