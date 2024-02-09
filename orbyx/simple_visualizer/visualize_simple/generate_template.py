import json
import os
import sys

from jinja2 import Environment, FileSystemLoader
from model.graph.graph import Graph
from services.visualizer_api import Visualizer

class SimpleVisualizer(Visualizer):

    def __init__(self):
        self.name = "Simple Visualizer"

    def get_name(self) -> str:
        return self.name
    def visualize(self, graph:Graph):
        # Specify the directory containing your Jinja2 templates
        current_directory = os.getcwd()
        # Get the parent directory (one level up)
        parent_directory = os.path.dirname(current_directory)
        app_templates_dir = os.path.join(parent_directory, 'simple_visualizer','build', 'lib', 'visualize_simple', 'templates')
        # Create a FileSystemLoader to load templates from the specified directory
        current_directory = os.getcwd()

        loader = FileSystemLoader(os.path.join(app_templates_dir))
        # Create a Jinja2 environment with the loader
        env = Environment(loader=loader)

        template_name = 'simple_graph.html'
        template = env.get_template(template_name)
        nodes = graph.serialize_nodes()
        edges = graph.serialize_edges()
        rendered_template = template.render({"nodes":json.dumps(nodes), "edges": json.dumps(edges)})
        return rendered_template
