import typing

from something.nodes import (
    EqualNode,
    FunctionNode,
    IdentifierNode,
    Node,
    SemicolonNode,
    gNode,
)


class GraphTraversal(Node):
    nodes: typing.List[Node] = [gNode()]

    def generate(self) -> typing.Generator[Node, None, None]:
        for node in self.nodes:
            yield node

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in self.generate())

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(FunctionNode("addE", [edgeLabel]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.nodes.append(FunctionNode("addV", [vertexLabel]))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(FunctionNode("has", [propertyKey, value]))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(FunctionNode("out", [edgeLabel]))
        return self

    def V(self) -> "GraphTraversal":
        self.nodes.append(FunctionNode("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.nodes.append(FunctionNode("values", [propertyKey]))
        return self


class Variable(Node):
    name: str
    nodes: typing.List[Node] = []

    def __init__(self, name: str):
        self.name = name

    def generate(self) -> typing.Generator[Node, None, None]:
        for node in self.nodes:
            yield node

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in (self.generate()))

    def assignment(self, g: GraphTraversal) -> "Variable":
        self.nodes.append(IdentifierNode(self.name))
        self.nodes.append(EqualNode())
        self.nodes.append(g)
        self.nodes.append(SemicolonNode())
        return self
