from typing import Any, Dict, List

from antlr4 import *
from java_parser import JavaParser
from java_lexer import JavaLexer
from api.services.data_source_api import DataSourceAPI
from api.model.graph import graph

from pprint import pprint
import config
import os

from dependency_listener import DependencyListener
class JavaDataSource(DataSourceAPI):
        def __init__(self):
            self.listener = DependencyListener()
        def parse_data(self, data: Any) -> List[Dict[str, Any]]:
                self.parse_java_file(data, self.listener)
        def get_data(self) -> graph.Graph:
            return super().get_data()
        def parse_java_file(self, file_path, listener):
            if("java" not in file_path):
                return
            input_stream = FileStream(file_path, config.encoding)
            lexer = JavaLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = JavaParser(token_stream)
            tree = parser.compilationUnit()

            walker = ParseTreeWalker()
            walker.walk(listener, tree)
        def process_files_in_directory(self, directory, listener):
            for root, dirs, files in os.walk(directory):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    self.parse_java_file(file_path, listener)

