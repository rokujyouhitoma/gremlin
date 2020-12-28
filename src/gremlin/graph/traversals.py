import typing
from dataclasses import dataclass, field

from gremlin.nodes import (
    IntegerNode,
    MethodCallNode,
    MultipleNode,
    Node,
    StringNode,
    gNode,
)


@dataclass
class GraphTraversal(MultipleNode):
    nodes: typing.List[Node] = field(default_factory=list)

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("addE", [StringNode(edgeLabel)]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("addV", [StringNode(vertexLabel)]))
        return self

    def aggregate(self, sideEffectKey: str = "") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("aggregate", [StringNode(sideEffectKey)]))
        return self

    def as_(self, stepLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("as", [StringNode(stepLabel)]))
        return self

    def by(self, *args: typing.Union[str, "GraphTraversal"]) -> "GraphTraversal":
        argument_list = [StringNode(v) if isinstance(v, str) else v for v in args]
        self.nodes.append(MethodCallNode("by", argument_list))
        return self

    def count(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("count", []))
        return self

    def groupCount(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("groupCount", []))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(
            MethodCallNode("has", [StringNode(propertyKey), StringNode(value)])
        )
        return self

    def hasLabel(self, label: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("hasLabel", [StringNode(label)]))
        return self

    def limit(self, limit: int) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("limit", [IntegerNode(limit)]))
        return self

    def in_(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("in", [StringNode(edgeLabel)]))
        return self

    def is_(self, value: typing.Any) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("is", [IntegerNode(value)]))
        return self

    def next(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("next", []))
        return self

    def not_(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("not", args))
        return self

    def match(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("match", args))
        return self

    def mean(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("mean", []))
        return self

    def pageRank(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("pageRank", []))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("out", [StringNode(edgeLabel)]))
        return self

    def order(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("order", args))
        return self

    def path(self) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("path", []))
        return self

    def repeat(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("repeat", args))
        return self

    def until(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("until", args))
        return self

    def select(self, selectKey: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("select", [StringNode(selectKey)]))
        return self

    def V(self) -> "GraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.nodes.append(MethodCallNode("values", [StringNode(propertyKey)]))
        return self

    def where(self, *args: "GraphTraversal") -> "GraphTraversal":
        self.nodes.append(MethodCallNode("where", args))
        return self
