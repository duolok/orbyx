from model.graph.graph_node import GraphNode
from typing import Optional

class GraphEdge:
    def __init__(self, origin, desination, value):
        self._origin = origin
        self._destination = desination
        self._value = value

    def endpoints(self):
        return (self._origin, self._destination)

    def value(self):
        return self._value

    def to_dict(self):
        return {"source":self._origin.node_value(), "target":self._destination.node_value(), "value": self._value}

    def __hash__(self):
        return hash((self._origin, self._destination))

    def __str__(self):
        return f"{self._origin}, {self._destination}, {self._value}"

