import json
from typing import Optional, TypeVar
from model.graph.graph_edge import GraphEdge
from model.graph.graph_node import GraphNode

class Graph:
    def __init__(self, directed=True):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def _validate_node(self, v):
        if not isinstance(v, GraphNode):
            raise TypeError("Expected object is class GraphNode.")
        if v not in self._outgoing:
            raise ValueError("Node doesn't belong to this graph.")

    def node_count(self):
        return len(self._outgoing)

    def nodes(self):
        return self._outgoing.keys()

    def serialize_nodes(self):
        nodes = list(self.nodes())
        ret = []
        for node in nodes:
            ret.append(json.dumps(node._value))
        return ret

        # return [json.dumps(node._value) for node in nodes]
    def serialize_edges(self):
        return [json.dumps(edge.to_dict()) for edge in self.edges()]

    def edge_count(self):
        return sum(len(secondary_map) for secondary_map in self._outgoing.values())

    def edges(self):
        return set(edge for secondary_map in self._outgoing.values() for edge in secondary_map.values())

    def is_directed(self):
        return self._incoming is not self._outgoing

    def get_edge(self, u, v):
        self._validate_node(u)
        self._validate_node(v)
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=False):
        self._validate_node(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=False):
        self._validate_node(v)
        adj = self._outgoing if outgoing else self._incoming
        return iter(adj[v].values())

    def insert_node(self, x=None):
        v = GraphNode(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:
            raise ValueError("U and v are already adjacent")
        e = GraphEdge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
