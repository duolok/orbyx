from abc import ABC, abstractmethod
from model.graph import graph
class Graph_Builder(ABC):
    #Abstract Graph building strategy
    @abstractmethod
    def build(self, nodes, edges) -> graph.Graph:
        pass
class Simple_Builder(Graph_Builder):
    #Graph Builder implementation that ignores multiple references
    def build(self, nodes, edges):
        g = graph.Graph()
        for k in nodes.keys():
            nodes[k]["node"] = g.insert_node(nodes[k]["data"])
        for edge in edges:
            try:
                g.insert_edge(nodes[edge[0]]["node"], nodes[edge[1]]["node"])
            except KeyError:
                #The second node of the edge is external to the project, therefore we don't have a declaration for it
                node2 = g.insert_node({"name" : edge[1], "fields" : [], "comment" : "THIS NODE IS EXTERNAL TO THE PROJECT"})
                nodes[edge[1]] = {"node" : node2,
                    "data" :{"name" : edge[1], "fields" : [], "comment" : "THIS NODE IS EXTERNAL TO THE PROJECT"}}
                g.insert_edge(nodes[edge[0]]["node"], node2)
            except ValueError:
                #This edge already exists, no need to add it again
                pass

        return g
class Weighed_Builder(Graph_Builder):
    #Graph Builder implementation that builds a weighed graph, where the weight of an edge is the number of references
    def build(self, nodes, edges):
        g = graph.Graph()
        for k in nodes.keys():
            nodes[k]["node"] = g.insert_node(nodes[k]["data"])
        for edge in edges:
            try:
                g.insert_edge(nodes[edge[0]]["node"], nodes[edge[1]]["node"], 1)
            except KeyError:
                #The second node of the edge is external to the project, therefore we don't have a declaration for it
                node2 = g.insert_node({"name" : edge[1], "fields" : [], "comment" : "THIS NODE IS EXTERNAL TO THE PROJECT"})
                nodes[edge[1]] = {"node" : node2,
                    "data" :{"name" : edge[1], "fields" : [], "comment" : "THIS NODE IS EXTERNAL TO THE PROJECT"}}
                g.insert_edge(nodes[edge[0]]["node"], node2, 1)
            except ValueError:
                g.get_edge(nodes[edge[0]]["node"], nodes[edge[1]]["node"])._value += 1
        return g