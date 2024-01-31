import os

from jinja2 import Environment, FileSystemLoader
from services.visualizer_api import Visualizer

class BlockVisualizer(Visualizer):
    def visualize(self, graph):
        # Specify the directory containing your Jinja2 templates
        current_directory = os.getcwd()
        # Get the parent directory (one level up)
        parent_directory = os.path.dirname(current_directory)
        app_templates_dir = os.path.join(parent_directory, 'block_visualizer', 'visualize', 'templates')
        # Create a FileSystemLoader to load templates from the specified directory
        loader = FileSystemLoader(os.path.join(app_templates_dir))

        # Create a Jinja2 environment with the loader
        env = Environment(loader=loader)

        template_name = 'block_graph.html'
        template = env.get_template(template_name)
        rendered_template = template.render()
        return rendered_template
