class GraphNode:
    def __init__(self, value):
        self._value = value

    def node_value(self):
        return self._value

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self._value)
