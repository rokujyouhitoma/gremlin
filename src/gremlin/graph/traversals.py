import typing
from abc import ABCMeta
from dataclasses import dataclass, field

from gremlin.nodes import (
    AnyNode,
    IntegerNode,
    MethodCallNode,
    MultipleNode,
    Node,
    StringNode,
    gNode,
)


class GraphTraversal(metaclass=ABCMeta):
    def addE(self, edgeLabel: str) -> "GraphTraversal":
        pass

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        pass

    def aggregate(self, sideEffectKey: str = "") -> "GraphTraversal":
        pass

    def as_(self, stepLabel: str) -> "GraphTraversal":
        pass

    def by(self, *args: typing.Union[str, "GraphTraversal"]) -> "GraphTraversal":
        pass

    def count(self) -> "GraphTraversal":
        pass

    def groupCount(self) -> "GraphTraversal":
        pass

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        pass

    def hasLabel(self, label: str) -> "GraphTraversal":
        pass

    def limit(self, limit: int) -> "GraphTraversal":
        pass

    def in_(self, edgeLabel: str) -> "GraphTraversal":
        pass

    def is_(self, value: typing.Any) -> "GraphTraversal":
        pass

    def next(self) -> "GraphTraversal":
        pass

    def not_(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def match(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def mean(self) -> "GraphTraversal":
        pass

    def pageRank(self) -> "GraphTraversal":
        pass

    def out(self, edgeLabel: str) -> "GraphTraversal":
        pass

    def order(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def path(self) -> "GraphTraversal":
        pass

    def repeat(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def until(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def select(self, selectKey: str) -> "GraphTraversal":
        pass

    def V(self) -> "GraphTraversal":
        pass

    def values(self, propertyKey: str) -> "GraphTraversal":
        pass

    def where(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass


@dataclass
class DefaultGraphTraversal(GraphTraversal, MultipleNode):
    nodes: typing.List[Node] = field(default_factory=list)

    def addE(self, edgeLabel: str) -> "DefaultGraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("addE", [StringNode(edgeLabel)]))
        return self

    def addV(self, vertexLabel: str = "") -> "DefaultGraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("addV", [StringNode(vertexLabel)]))
        return self

    def aggregate(self, sideEffectKey: str = "") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("aggregate", [StringNode(sideEffectKey)]))
        return self

    def as_(self, stepLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("as", [StringNode(stepLabel)]))
        return self

    def by(self, *args: typing.Union[str, "GraphTraversal"]) -> "DefaultGraphTraversal":
        argument_list = [
            StringNode(v) if isinstance(v, str) else AnyNode(v) for v in args
        ]
        self.nodes.append(MethodCallNode("by", argument_list))
        return self

    def count(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("count", []))
        return self

    def groupCount(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("groupCount", []))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("has", [StringNode(propertyKey), StringNode(value)])
        )
        return self

    def hasLabel(self, label: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("hasLabel", [StringNode(label)]))
        return self

    def limit(self, limit: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("limit", [IntegerNode(limit)]))
        return self

    def in_(self, edgeLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("in", [StringNode(edgeLabel)]))
        return self

    def is_(self, value: typing.Any) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("is", [IntegerNode(value)]))
        return self

    def next(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("next", []))
        return self

    def not_(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("not", argument_list))
        return self

    def match(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("match", argument_list))
        return self

    def mean(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("mean", []))
        return self

    def pageRank(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("pageRank", []))
        return self

    def out(self, edgeLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("out", [StringNode(edgeLabel)]))
        return self

    def order(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("order", argument_list))
        return self

    def path(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("path", []))
        return self

    def repeat(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("repeat", argument_list))
        return self

    def until(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("until", argument_list))
        return self

    def select(self, selectKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("select", [StringNode(selectKey)]))
        return self

    def V(self) -> "DefaultGraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("V", []))
        return self

    def values(self, propertyKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("values", [StringNode(propertyKey)]))
        return self

    def where(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        argument_list = [AnyNode(v) for v in args]
        self.nodes.append(MethodCallNode("where", argument_list))
        return self
