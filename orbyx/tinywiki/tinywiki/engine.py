import os
import sys

from model.graph.graph import Graph
from services.data_source_api import DataSourceAPI
from scraper import *

class WikipediaDataSource(DataSourceAPI):
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        #start_url = data[0]
        start_url = "https://en.wikipedia.org/wiki/Rust_(programming_language)"
        scraped_dictionary = get_scraped_dictionary(start_url)
        return [{key: val} for key, val in scraped_dictionary.items()]

    def get_graph(self, parsed_data: List[Dict[str, Any]]) -> Graph:
        graph = Graph()
        data_dict = {list(page_data.keys())[0]: list(page_data.values())[0] for page_data in parsed_data}

        for url, page_data in data_dict.items():
            name = page_data["name"]
            paragraphs = page_data["paragraphs"]
            graph.insert_node({"name": name, "paragraphs": paragraphs})

            for child_url in page_data["children"]:
                if child_url in data_dict:  
                    child_name = data_dict[child_url]["name"]
                    graph.insert_edge(name, child_name)
        return graph

def main():
    wikipedia_data_source = WikipediaDataSource()
    parsed_data = wikipedia_data_source.parse_data(None)  
    graph = wikipedia_data_source.get_graph(parsed_data)

    print("Graph Nodes:")
    for node in graph.get_nodes():
        print(f"Node: {node['name']}, Paragraphs: {len(node['paragraphs'])}")

    print("\nGraph Edges:")
    for edge in graph.get_edges():
        print(f"Edge: {edge}")

if __name__ == "__main__":
    main()
