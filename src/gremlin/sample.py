import typing
from dataclasses import dataclass, field

from gremlin.nodes import (
    ArgumentListNode,
    AssignmentStatement,
    CallNameNode,
    CallNode,
    IdentifierNode,
    IntegerNode,
    MethodCallNode,
    MethodCallNodeArgumentsNode,
    MultipleNode,
    Node,
    StringNode,
)


@dataclass
class GraphTraversal(MultipleNode):
    nodes: typing.List[Node] = field(default_factory=list)

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("addE", [StringNode(edgeLabel)]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("addV", [StringNode(vertexLabel)]))
        return self

    def as_(self, stepLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("as", [StringNode(stepLabel)]))
        return self

    def by(self, key: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("by", [StringNode(key)]))
        return self

    def count(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("count", []))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(
            MethodCallNode("has", [StringNode(propertyKey), StringNode(value)])
        )
        return self

    def in_(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("in", [StringNode(edgeLabel)]))
        return self

    def is_(self, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("is", [IntegerNode(value)]))
        return self

    def match(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNodeArgumentsNode("match", args))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("out", [StringNode(edgeLabel)]))
        return self

    def path(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("path", []))
        return self

    def repeat(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNodeArgumentsNode("repeat", args))
        return self

    def until(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNodeArgumentsNode("until", args))
        return self

    def select(self, selectKey: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("select", [StringNode(selectKey)]))
        return self

    def V(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("values", [StringNode(propertyKey)]))
        return self


@dataclass
class Variable(MultipleNode):
    name: str

    def assignment(self, node: Node) -> "Variable":
        self.nodes.append(AssignmentStatement(IdentifierNode(self.name), node))
        return self


def as_(stepLabel: str) -> GraphTraversal:
    return GraphTraversal(
        [CallNode(CallNameNode("as"), ArgumentListNode([StringNode(stepLabel)]))]
    )


def has(propertyKey: str, value: typing.Any) -> GraphTraversal:
    return GraphTraversal(
        [
            CallNode(
                CallNameNode("has"),
                ArgumentListNode([StringNode(propertyKey), StringNode(value)]),
            )
        ]
    )


def in_(edgeLabel: str) -> GraphTraversal:
    return GraphTraversal(
        [CallNode(CallNameNode("in"), ArgumentListNode([StringNode(edgeLabel)]))]
    )
