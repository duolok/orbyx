from graph_node import GraphNode
from typing import Optional

class GraphEdge:
    def __init__(self, origin, desination, value):
        self._origin = origin
        self._destination = desination
        self._value = value

    def opposite(self, v: N) -> Optional[N]:
        """Return the opposite endpoint of the given node."""
        if v == self._destination:
            return self._origin
        elif v == self._origin:
            return self._destination
        else:
            raise ValueError("Provided node is not an endpoint of this edge")

    def endpoints(self):
        return (self._origin, self._destination)

    def value(self):
        return self._value

    def __hash__(self):
        return hash((self._origin, self._destination))

   def __str__(self):
        return f"{self._origin}, {self._destination}, {self._value}"
