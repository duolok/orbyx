from model.graph.graph import Graph
from model.graph.graph import GraphEdge
from model.graph.graph import GraphNode
from typing import Any, List, Dict
from search.utils import ops
class SearchProvider():
    def __init__(self, initial_graph: Graph):
        self.sub_graph = initial_graph
        self.initial_graph = initial_graph
        self.working_graph = Graph()
        self.added_nodes = {}
        self.back_stack = []

    def search(self, search_term):
        self._search_edges(search_term)
        return self.sub_graph
    def filter(self, filter):
        self._filter_edges(filter)
        return self.sub_graph
    
    def _check_term(self, search_term : str, node : GraphNode):
        for k in node.node_value():
            if search_term.upper() in k.upper():
                return True
            if search_term.upper() in str(node.node_value()[k]).upper():
                return True
        return False
    def _search_edges(self, search_term):
        self.working_graph = Graph()
        self.added_nodes = {}
        removed_edges = []
        removed_nodes = []
        for edge in self.sub_graph.edges():
            
            (e1, e2) = edge.endpoints()
            node1 = None
            node2 = None
            if (self._check_term(search_term, e1)):
                if(str(e1.node_value()) in self.added_nodes.keys()):
                    node1 = self.added_nodes[str(e1.node_value())]
                else:
                    node1 = self.working_graph.insert_node(e1.node_value())
                    self.added_nodes[str(e1.node_value())] = node1
            if (self._check_term(search_term, e2)):
                if(str(e2.node_value()) in self.added_nodes.keys()):
                    node2 = self.added_nodes[str(e2.node_value())]
                else:
                    node2 = self.working_graph.insert_node(e2.node_value())
                    self.added_nodes[str(e2.node_value())] = node2
            if (node1 and node2):
                try:
                    self.working_graph.insert_edge(node1, node2, edge.value())
                except Exception as e:
                    print(e)
            else:
                removed_edges.append(edge)
        for node in self.sub_graph.nodes():
            if str(node.node_value()) not in self.added_nodes.keys():
                if (self._check_term(search_term, node)):
                    node2 = self.working_graph.insert_node(node.node_value())
                    self.added_nodes[str(node.node_value())] = node2
                else:
                    removed_nodes.append(node)
        self.sub_graph = self.working_graph
        self.back_stack.append([["S", search_term], removed_edges, removed_nodes])
    def reset(self):
        self.added_nodes = {}
        self.sub_graph = self.initial_graph
        return self.sub_graph

    def undo(self):
        self.added_nodes = {}
        undone_nodes = []

        if(len(self.back_stack) == 0):
            raise Exception("BackStack Empty")
        [term, edges, nodes] = self.back_stack.pop()
        for edge in edges:
            (e1, e2) = edge.endpoints()
            for node in self.sub_graph.nodes():
                if(node.node_value() == e1.node_value()):
                    e1 = node
                if(node.node_value() == e2.node_value()):
                    e2 = node
            try:
                self.sub_graph._validate_node(e1)
            except:
                e1 = self.sub_graph.insert_node(e1.node_value())
                undone_nodes.append(str(e1.node_value()))
            try:
                self.sub_graph._validate_node(e2)
            except:
                e2 = self.sub_graph.insert_node(e2.node_value())
                undone_nodes.append(str(e2.node_value()))
            self.sub_graph.insert_edge(e1, e2, edge.value())
        for n in nodes:
            if str(n.node_value()) not in undone_nodes:
                self.sub_graph.insert_node(n.node_value())
        return self.sub_graph

    def _parse_filter(self, filter:str):
        filter = filter.split(" ")
        if (len(filter) != 3 or filter[1] not in ops):
            raise Exception("Illegal filter")
        return filter
    
    def _apply_filter(self, node : GraphNode, key : str, value, operation: str) -> bool:
        vals = node.node_value()
        if (key not in vals.keys()):
            return False
        converted_value = None
        try:
            value = eval(value)
        except Exception:
            raise ValueError("Expected number type as filter term")
        if not (isinstance(vals[key], int) or isinstance(vals[key], float)):
            try:
                converted_value = eval(vals[key])
            except Exception as e:
                
                print(vals[key])
                return False
                ##In this case, the passed attribute cannot be compared with the passed value, therefore we treat it as not passing the filter rather than raising an exception
        else:
            converted_value = vals[key]
        return ops[operation](converted_value, value)
    def _filter_edges(self, search_term):
        (key, operation, value) = self._parse_filter(search_term)
        removed_edges = []
        removed_nodes = []
        self.added_nodes = {}

        self.working_graph = Graph()
        for edge in self.sub_graph.edges():
            (e1, e2) = edge.endpoints()
            node1 = None
            node2 = None
            if (self._apply_filter(e1, key, value, operation)):
                if(str(e1.node_value()) in self.added_nodes.keys()):
                    node1 = self.added_nodes[str(e1.node_value())]
                else:
                    node1 = self.working_graph.insert_node(e1.node_value())
                    self.added_nodes[str(e1.node_value())] = node1
            if (self._apply_filter(e2, key, value, operation)):
                if(str(e2.node_value()) in self.added_nodes.keys()):
                    node2 = self.added_nodes[str(e2.node_value())]
                else:
                    node2 = self.working_graph.insert_node(e2.node_value())
                    self.added_nodes[str(e2.node_value())] = node2
            if (node1 and node2):
                try:
                    self.working_graph.insert_edge(node1, node2, edge.value())
                except Exception as e:
                    print(e)
            else:
                removed_edges.append(edge)
        not_added_nodes = []
        for node in self.sub_graph.nodes():
            if str(node.node_value()) not in self.added_nodes.keys():
                if self._apply_filter(node, key, value, operation):
                    not_added_nodes.append(node)
                else:
                    removed_nodes.append(node)
        for node in not_added_nodes:
            self.working_graph.insert_node(node.node_value())
        self.sub_graph = self.working_graph
        self.back_stack.append([["F", search_term], removed_edges, removed_nodes])
    def reinitialize(self):
        for operation in self.back_stack:
            if operation[0] == "F":
                self.filter(operation[1])
            elif operation[0] == "S":
                self.search(operation[1])