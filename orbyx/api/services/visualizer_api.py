from abc import ABC, abstractmethod
from typing import Any

class Visualizer(ABC):
    @abstractmethod
    def visualize(self, graph: Any) -> Any:
        """Abstract method for data visualization"""
        pass
