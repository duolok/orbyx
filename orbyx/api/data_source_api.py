from abc import ABC, abstractmethod
from typing import Any, Dict, List

class DataSourceAPI(ABC):
    @abstractmethod
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_data(self) -> Graph:
        pass
