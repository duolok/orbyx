from typing import Any, Dict, List

from antlr4 import *
from java_data_source.antlr import java_parser
from java_data_source.antlr import java_lexer
#from api.services.data_source_api import DataSourceAPI
#from api.model.graph import graph
from services.data_source_api import DataSourceAPI
from model.graph import graph
from java_data_source.graph_builder import graph_builder

from java_data_source import config
import os

from java_data_source.dependency_listener import DependencyListener
class JavaDataSource(DataSourceAPI):
        def __init__(self):
            self.listener = DependencyListener()
            self.builder: graph_builder.Graph_Builder = graph_builder.Simple_Builder()
        def parse_data(self, data: Any) -> List[Dict[str, Any]]:
            config.path = data['project_url']
            self.process_files_in_directory(config.path)
            return [self.listener.nodes, self.listener.edges]
        @property
        def name(self) -> str:
            return "Java Parser"
        def get_name(self) -> str:
            return "Java Parser"
        def get_requirements(self) -> List:         
            fields = [             
                {'name': 'project_url', 'label': 'Project URL'}]         
            return fields
     
        def get_graph(self, parsed_data: List[Dict[str, Any]]) -> graph.Graph:
            return self.builder.build(self.listener.nodes, self.listener.edges)
        def parse_java_file(self, file_path):
            if("java" not in file_path):
                return
            input_stream = FileStream(file_path, config.encoding)
            lexer = java_lexer.JavaLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = java_parser.JavaParser(token_stream)
            tree = parser.compilationUnit()

            walker = ParseTreeWalker()
            walker.walk(self.listener, tree)
        def process_files_in_directory(self, directory):
            for root, dirs, files in os.walk(directory):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    self.parse_java_file(file_path)
                
