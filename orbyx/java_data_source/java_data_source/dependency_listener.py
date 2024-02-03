from antlr4 import *
from pprint import pprint
from api.model.graph import graph

class DependencyListener(ParseTreeListener):
    def __init__(self):
        self.graph = graph.Graph()
        self.current_class = None
        self.current_package = None
    def enterInterfaceDeclaration(self, ctx):
        
        class_name = ctx.identifier().getText()
        self.current_class = class_name
        self.graph.add_node(class_name)
        if(self.current_package):
            self.graph.add_edge(self.current_package, class_name)
    def enterClassDeclaration(self, ctx):
        
        class_name = ctx.identifier().getText()
        self.current_class = class_name
        self.graph.add_node(class_name)

        if(self.current_package):
            self.graph.add_edge(self.current_package, class_name)
    def enterPackageDeclaration(self, ctx):
        self.current_package = '.'.join(identifier.getText() for identifier in  ctx.qualifiedName().identifier())

        self.graph.add_node(self.current_package)
    def exitPackageDeclaration(self, ctx):
        for subPackage in self.current_package.split("."):
            if subPackage in self.graph.nodes and subPackage != self.current_package:
                self.graph.add_edge(subPackage, self.current_package)
    def exitClassDeclaration(self, ctx):
        self.current_class = None
    def exitInterfaceDeclaration(self, ctx):
        self.current_class = None
    def enterTypeTypeOrVoid(self, ctx):
        if self.current_class is not None:
            type_name = ctx.getText()
            if '.' in type_name:
                # Extract the class name from the fully qualified name
                type_name = type_name.split('.')[-1]
            if type_name != self.current_class:
                self.graph.add_edge(self.current_class, type_name)
                print(self.current_class, type_name)



