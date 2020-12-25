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
    identifier: IdentifierNode
    graph_traversal: GraphTraversal
    equal_node: EqualNode
    semicolon_node: SemicolonNode

    def __init__(self, identifier: IdentifierNode, graph_traversal: GraphTraversal):
        self.identifier = identifier
        self.graph_traversal = graph_traversal
        self.equal_node = EqualNode()
        self.semicolon_node = SemicolonNode()
        self.nodes = [
            self.identifier,
            self.equal_node,
            self.graph_traversal,
            self.semicolon_node,
        ]


@dataclass
class Variable(MultipleNode):
    name: str

    def assignment(self, graph_traversal: GraphTraversal) -> "Variable":
        self.nodes.append(
            AssignmentStatement(IdentifierNode(self.name), graph_traversal)
        )
        return self
