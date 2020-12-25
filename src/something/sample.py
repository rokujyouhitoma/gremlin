import typing
from dataclasses import dataclass

from something.nodes import (
    EqualNode,
    IdentifierNode,
    MethodCallNode,
    MultipleNode,
    Node,
    SemicolonNode,
    gNode,
)


class GraphTraversal(MultipleNode):
    nodes: typing.List[Node] = [gNode()]

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("addE", [edgeLabel]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("addV", [vertexLabel]))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("has", [propertyKey, value]))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("out", [edgeLabel]))
        return self

    def V(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("values", [propertyKey]))
        return self


class AssignmentStatement(MultipleNode):
    def __init__(self, identifier: IdentifierNode, node: Node):
        self.nodes = [
            identifier,
            EqualNode(),
            node,
            SemicolonNode(),
        ]


@dataclass
class Variable(MultipleNode):
    name: str

    def assignment(self, node: Node) -> "Variable":
        self.nodes.append(AssignmentStatement(IdentifierNode(self.name), node))
        return self
