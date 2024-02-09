from antlr4 import *
from model.graph import graph

class DependencyListener(ParseTreeListener):
    def __init__(self):
        self.graph = graph.Graph()
        self.nodes = {}
        self.current_class = None
        self.current_package = None
        self.data = {}
        self.edges = []
        
    def enterInterfaceDeclaration(self, ctx):
        
        class_name = ctx.identifier().getText()
        self.current_class = class_name
        self.insert_node(class_name, self.data)
        if(self.current_package):
            self.insert_edge(self.current_package, class_name)
    def enterClassDeclaration(self, ctx):
        
        class_name = ctx.identifier().getText()
        self.current_class = class_name
        self.insert_node(class_name, self.data)

        if(self.current_package):
            self.insert_edge(self.current_package, class_name)
    def enterEnumDeclaration(self, ctx):
        
        class_name = ctx.identifier().getText()
        self.current_class = class_name
        self.insert_node(class_name, self.data)

        if(self.current_package):
            self.insert_edge(self.current_package, class_name)
    def exitEnumDeclaration(self, ctx):
        self.current_class = None
    def enterFieldDeclaration(self, ctx):
        if ctx.typeType().primitiveType() == None:
            self.nodes[self.current_class]["data"]["fields"].append([ctx.typeType().classOrInterfaceType().getText(), ctx.variableDeclarators().variableDeclarator(0).variableDeclaratorId().identifier().getText()])
            return
        self.nodes[self.current_class]["data"]["fields"].append([ctx.typeType().primitiveType().getText(), ctx.variableDeclarators().variableDeclarator(0).variableDeclaratorId().identifier().getText()])

    def enterPackageDeclaration(self, ctx):
        self.current_package = '.'.join(identifier.getText() for identifier in  ctx.qualifiedName().identifier())

        self.insert_node(self.current_package, self.data)
    def exitPackageDeclaration(self, ctx):
        for subPackage in self.current_package.split("."):
            if subPackage in self.graph.nodes() and subPackage != self.current_package:
                self.insert_edge(subPackage, self.current_package)
    def exitClassDeclaration(self, ctx):
        self.current_class = None
    def exitInterfaceDeclaration(self, ctx):
        self.current_class = None
    def enterTypeTypeOrVoid(self, ctx):
        if self.current_class is not None:
            type_name = ctx.getText()
            if '.' in type_name:
                type_name = type_name.split('.')[-1]
            if type_name != self.current_class and type_name!='void':
                self.insert_edge(self.current_class, type_name)

    def insert_node(self, name, data):
        if(name in self.nodes.keys()):
            return
        data["name"] = name
        self.nodes[name] = {
            "node" : None,
            "data" : {
                "name" : name
            }
        }
        self.nodes[name]["data"]["fields"] = []
    def getNode(self, name):
        return self.nodes[name]["node"]
    def insert_edge(self, name1, name2):
        self.edges.append([name1, name2])
     