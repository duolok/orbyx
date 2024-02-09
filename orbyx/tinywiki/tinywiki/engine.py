import os
import sys

from model.graph.graph import Graph, GraphNode
from services.data_source_api import DataSourceAPI
from tinywiki.scraper import get_scraped_dictionary
from typing import Any, List, Dict

class WikipediaDataSource(DataSourceAPI):
    def __init__(self):
        self.name = "Tinywiki"

    def get_name(self) -> str:
        return self.name
    
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        start_url, max_nodes = data['start_url'], data['max_nodes']
        scraped_dictionary = get_scraped_dictionary(start_url, max_nodes)
        return [{key: val} for key, val in scraped_dictionary.items()]

    def get_graph(self, parsed_data: List[Dict[str, Any]]) -> Graph:
        graph = Graph()
        vertex_map = {}
        i = 1
        for page_data in parsed_data:
            url = list(page_data.keys())[0]
            page_info = list(page_data.values())[0]
            name = page_info["name"]
            paragraphs = page_info["paragraphs"]
            children = page_info["children"]

            node_value = {
                "id":i,
                "url": url,
                "name": name,
                "paragraphs": paragraphs,
                "children": len(children)
            }
            i+=1
            # node = GraphNode(node_value)
            vertex = graph.insert_node(node_value)
            vertex_map[url] = vertex

        for page_data in parsed_data:
            url = list(page_data.keys())[0]
            page_info = list(page_data.values())[0]

            for child_url in page_info["children"]:
                parent_vertex = vertex_map[url]
                child_vertex = vertex_map[child_url]
                if graph.get_edge(parent_vertex, child_vertex) is None:
                    graph.insert_edge(parent_vertex, child_vertex)

        return graph
