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
from gremlin.structures import List


class Traversal(metaclass=ABCMeta):
    def iterate(self) -> "Traversal":
        pass

    def next(self, amount: int) -> List:
        pass

    def none(self) -> "Traversal":
        pass

    def toList(self) -> "Traversal":
        # TODO: Should support for -> default List<E>
        pass

    def toSet(self) -> "Traversal":
        # TODO: Should support for -> default Set<E>
        pass


class GraphTraversal(metaclass=ABCMeta):
    def addE(self, edgeLabel: typing.Union[str, "GraphTraversal"]) -> "GraphTraversal":
        pass

    def addV(
        self, vertexLabel: typing.Union[str, "GraphTraversal", None]
    ) -> "GraphTraversal":
        pass

    def aggregate(self, sideEffectKey: str) -> "GraphTraversal":
        pass

    def and_(self, *andTraversals: "GraphTraversal") -> "GraphTraversal":
        pass

    def as_(self, stepLabel: str, *stepLabels: str) -> "GraphTraversal":
        pass

    def asAdmin(self) -> "GraphTraversal":
        pass

    def barrier(self, maxBarrierSize: typing.Optional[int]) -> "GraphTraversal":
        pass

    def both(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def bothE(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def bothV(self) -> "GraphTraversal":
        pass

    def branch(self, branchTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def by(self, *args: typing.Union[str, "GraphTraversal"]) -> "GraphTraversal":
        # TODO: too many arguments variation is exist
        pass

    def cap(self, sideEffectKey: str, *sideEffectKeys: str) -> "GraphTraversal":
        pass

    def choose(self, choiceTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def coalesce(self, coalesceTraversals: "GraphTraversal") -> "GraphTraversal":
        pass

    def coin(self, probability: int) -> "GraphTraversal":
        pass

    def connectedComponent(self) -> "GraphTraversal":
        pass

    def count(self) -> "GraphTraversal":
        pass

    def cyclicPath(self) -> "GraphTraversal":
        pass

    def dedup(self, *dedupLabels: str) -> "GraphTraversal":
        pass

    def drop(self) -> "GraphTraversal":
        pass

    def elementMap(self, *propertyKeys: str) -> "GraphTraversal":
        pass

    def groupCount(self) -> "GraphTraversal":
        pass

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        pass

    def hasLabel(self, label: str, *otherLabels: str) -> "GraphTraversal":
        pass

    def id(self) -> "GraphTraversal":
        pass

    def index(self) -> "GraphTraversal":
        pass

    def inE(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def inV(self) -> "GraphTraversal":
        pass

    def in_(self, edgeLabel: str) -> "GraphTraversal":
        pass

    def is_(self, value: typing.Any) -> "GraphTraversal":
        pass

    def iterate(self) -> "GraphTraversal":
        pass

    def key(self) -> "GraphTraversal":
        pass

    def label(self) -> "GraphTraversal":
        pass

    def limit(self, limit: int) -> "GraphTraversal":
        pass

    def match(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def max(self) -> "GraphTraversal":
        pass

    def mean(self) -> "GraphTraversal":
        pass

    def min(self) -> "GraphTraversal":
        pass

    def not_(self, notTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def or_(self, orTraversals: "GraphTraversal") -> "GraphTraversal":
        pass

    def order(self, *args: "GraphTraversal") -> "GraphTraversal":
        # TODO: Should support for order() and order(Scope scope)
        pass

    def otherV(self) -> "GraphTraversal":
        pass

    def out(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def outE(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def outV(self) -> "GraphTraversal":
        pass

    def pageRank(self) -> "GraphTraversal":
        pass

    def path(self) -> "GraphTraversal":
        pass

    def repeat(
        self,
        loopName: typing.Union[str, "GraphTraversal"],
        repeatTraversal: typing.Optional["GraphTraversal"],
    ) -> "GraphTraversal":
        pass

    def select(self, selectKey: str) -> "GraphTraversal":
        pass

    def until(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def V(self) -> "GraphTraversal":
        pass

    def value(self) -> "GraphTraversal":
        pass

    def valueMap(self, *propertyKeys: str) -> "GraphTraversal":
        pass

    def values(self, propertyKey: str) -> "GraphTraversal":
        pass

    def where(self, whereTraversal: "GraphTraversal") -> "GraphTraversal":
        pass


@dataclass
class DefaultGraphTraversal(Traversal, GraphTraversal, MultipleNode):
    nodes: typing.List[Node] = field(default_factory=list)

    def addE(
        self, edgeLabel: typing.Union[str, "GraphTraversal"]
    ) -> "DefaultGraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(
            MethodCallNode(
                "addE",
                [
                    StringNode(edgeLabel)
                    if isinstance(edgeLabel, str)
                    else AnyNode(edgeLabel)
                ],
            )
        )
        return self

    def addV(
        self, vertexLabel: typing.Union[str, "GraphTraversal", None] = None
    ) -> "DefaultGraphTraversal":
        self.nodes = [gNode()]
        self.nodes.append(
            MethodCallNode(
                "addV",
                []
                if vertexLabel is None
                else [
                    StringNode(vertexLabel)
                    if isinstance(vertexLabel, str)
                    else AnyNode(vertexLabel)
                ],
            )
        )
        return self

    def aggregate(self, sideEffectKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("aggregate", [StringNode(sideEffectKey)]))
        return self

    def and_(self, *andTraversals: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("and", [AnyNode(v) for v in andTraversals]))
        return self

    def as_(self, stepLabel: str, *stepLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("as", [StringNode(v) for v in (stepLabel, *stepLabels)])
        )
        return self

    def asAdmin(self) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "asAdmin",
                [],
            )
        )
        return self

    def barrier(
        self, maxBarrierSize: typing.Optional[int] = None
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "barrier",
                [] if maxBarrierSize is None else [IntegerNode(maxBarrierSize)],
            )
        )
        return self

    def both(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "both",
                [StringNode(v) for v in edgeLabels],
            )
        )
        return self

    def bothE(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "bothE",
                [StringNode(v) for v in edgeLabels],
            )
        )
        return self

    def bothV(self) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "bothV",
                [],
            )
        )
        return self

    def branch(self, branchTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "branch",
                [AnyNode(branchTraversal)],
            )
        )
        return self

    def by(self, *args: typing.Union[str, "GraphTraversal"]) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "by",
                [StringNode(v) if isinstance(v, str) else AnyNode(v) for v in args],
            )
        )
        return self

    def cap(self, sideEffectKey: str, *sideEffectKeys: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "cap", [StringNode(v) for v in (sideEffectKey, *sideEffectKeys)]
            )
        )
        return self

    def choose(self, choiceTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "choose",
                [AnyNode(choiceTraversal)],
            )
        )
        return self

    def coalesce(self, coalesceTraversals: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "coalesce",
                [AnyNode(coalesceTraversals)],
            )
        )
        return self

    def coin(self, probability: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("coin", [IntegerNode(probability)]))
        return self

    def connectedComponent(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("connectedComponent", []))
        return self

    def count(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("count", []))
        return self

    def cyclicPath(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("cyclicPath", []))
        return self

    def dedup(self, *dedupLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "dedup",
                [StringNode(v) for v in dedupLabels],
            )
        )
        return self

    def drop(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("drop", []))
        return self

    def elementMap(self, *propertyKeys: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "elementMap",
                [StringNode(v) for v in propertyKeys],
            )
        )
        return self

    def groupCount(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("groupCount", []))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("has", [StringNode(propertyKey), StringNode(value)])
        )
        return self

    def hasLabel(self, label: str, *otherLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("hasLabel", [StringNode(v) for v in (label, *otherLabels)])
        )
        return self

    def id(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("id", []))
        return self

    def in_(self, edgeLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("in", [StringNode(edgeLabel)]))
        return self

    def index(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("index", []))
        return self

    def inE(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("inE", [StringNode(v) for v in edgeLabels]))
        return self

    def inV(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("inV", []))
        return self

    def is_(self, value: typing.Any) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("is", [IntegerNode(value)]))
        return self

    def iterate(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("iterate", []))
        return self

    def key(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("key", []))
        return self

    def label(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("label", []))
        return self

    def limit(self, limit: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("limit", [IntegerNode(limit)]))
        return self

    def match(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("match", [AnyNode(v) for v in args]))
        return self

    def max(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("max", []))
        return self

    def mean(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("mean", []))
        return self

    def min(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("min", []))
        return self

    def next(self, amount: int = 0) -> List:
        args = [] if amount == 0 else [IntegerNode(amount)]
        self.nodes.append(MethodCallNode("next", args))
        return List(self.nodes)

    def none(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("none", []))
        return self

    def not_(self, notTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("not", [AnyNode(notTraversal)]))
        return self

    def or_(self, orTraversals: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("or", [AnyNode(orTraversals)]))
        return self

    def order(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        # TODO: Should support for order() and order(Scope scope)
        self.nodes.append(MethodCallNode("order", [AnyNode(v) for v in args]))
        return self

    def otherV(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("otherV", []))
        return self

    def out(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("out", [StringNode(v) for v in edgeLabels]))
        return self

    def outE(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("outE", [StringNode(v) for v in edgeLabels]))
        return self

    def outV(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("outV", []))
        return self

    def pageRank(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("pageRank", []))
        return self

    def path(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("path", []))
        return self

    def repeat(
        self,
        loopName: typing.Union[str, "GraphTraversal"],
        repeatTraversal: typing.Optional["GraphTraversal"] = None,
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "repeat",
                [StringNode(typing.cast(str, loopName)), AnyNode(repeatTraversal)]
                if repeatTraversal is not None
                else [AnyNode(loopName)],
            )
        )
        return self

    def select(self, selectKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("select", [StringNode(selectKey)]))
        return self

    def toList(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("toList", []))
        return self

    def toSet(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("toSet", []))
        return self

    def until(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("until", [AnyNode(v) for v in args]))
        return self

    def V(self) -> "DefaultGraphTraversal":
        # TODO: ???
        self = DefaultGraphTraversal()
        self.nodes = [gNode()]
        self.nodes.append(MethodCallNode("V", []))
        return self

    def value(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("value", []))
        return self

    def valueMap(self, *propertyKeys: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("valueMap", [StringNode(v) for v in propertyKeys])
        )
        return self

    def values(self, propertyKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("values", [StringNode(propertyKey)]))
        return self

    def where(self, whereTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("where", [AnyNode(whereTraversal)]))
        return self
