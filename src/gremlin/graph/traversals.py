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

    def emit(self) -> "GraphTraversal":
        pass

    def filter(self, filterTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def flatMap(self, flatMapTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def fold(self) -> "GraphTraversal":
        pass

    def from_(self, fromStepLabel: str) -> "GraphTraversal":
        pass

    def group(self, sideEffectKey: typing.Optional[str] = None) -> "GraphTraversal":
        pass

    def groupCount(
        self, sideEffectKey: typing.Optional[str] = None
    ) -> "GraphTraversal":
        pass

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        pass

    def hasId(self, id: str, *otherIds: str) -> "GraphTraversal":
        pass

    def hasKey(self, label: str, *otherLabels: str) -> "GraphTraversal":
        pass

    def hasLabel(self, label: str, *otherLabels: str) -> "GraphTraversal":
        pass

    def hasNot(self, propertyKey: str) -> "GraphTraversal":
        pass

    def hasValue(self, value: str, *otherValues: str) -> "GraphTraversal":
        pass

    def id(self) -> "GraphTraversal":
        pass

    def identity(self) -> "GraphTraversal":
        pass

    def in_(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def index(self) -> "GraphTraversal":
        pass

    def inE(self, *edgeLabels: str) -> "GraphTraversal":
        pass

    def inV(self) -> "GraphTraversal":
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

    def local(self, localTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def loops(self, loopName: typing.Optional[str] = None) -> "GraphTraversal":
        pass

    def map(self, mapTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def match(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def math(self, expression: str) -> "GraphTraversal":
        pass

    def max(self) -> "GraphTraversal":
        pass

    def mean(self) -> "GraphTraversal":
        pass

    def min(self) -> "GraphTraversal":
        pass

    def none(self) -> "GraphTraversal":
        pass

    def not_(self, notTraversal: "GraphTraversal") -> "GraphTraversal":
        pass

    def option(self, traversalOption: "GraphTraversal") -> "GraphTraversal":
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

    def peerPressure(self) -> "GraphTraversal":
        pass

    def profile(self) -> "GraphTraversal":
        pass

    def project(self, projectKey: str, *otherProjectKeys: str) -> "GraphTraversal":
        pass

    def repeat(
        self,
        loopName: typing.Union[str, "GraphTraversal"],
        repeatTraversal: typing.Optional["GraphTraversal"],
    ) -> "GraphTraversal":
        pass

    def sack(self) -> "GraphTraversal":
        pass

    def sample(self, amountToSample: int) -> "GraphTraversal":
        pass

    def select(self, selectKey: str) -> "GraphTraversal":
        pass

    def shortestPath(self) -> "GraphTraversal":
        pass

    def simplePath(self) -> "GraphTraversal":
        pass

    def skip(self, skip: int) -> "GraphTraversal":
        pass

    def subgraph(self, sideEffectKey: str) -> "GraphTraversal":
        pass

    def sum(self) -> "GraphTraversal":
        pass

    def tail(self) -> "GraphTraversal":
        pass

    def timeLimit(self, timeLimit: int) -> "GraphTraversal":
        pass

    def times(self, maxLoops: int) -> "GraphTraversal":
        pass

    def to(self, toStepLabel: str) -> "GraphTraversal":
        pass

    def tree(self, sideEffectKey: typing.Optional[str] = None) -> "GraphTraversal":
        pass

    def until(self, *args: "GraphTraversal") -> "GraphTraversal":
        pass

    def unfold(self) -> "GraphTraversal":
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

    def with_(self, key: str) -> "GraphTraversal":
        pass

    def write(self) -> "GraphTraversal":
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

    def emit(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("emit", []))
        return self

    def filter(self, filterTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("filter", [AnyNode(filterTraversal)]))
        return self

    def flatMap(self, flatMapTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("flatMap", [AnyNode(flatMapTraversal)]))
        return self

    def fold(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("fold", []))
        return self

    def from_(self, fromStepLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("from", [StringNode(fromStepLabel)]))
        return self

    def group(
        self, sideEffectKey: typing.Optional[str] = None
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "group",
                [] if sideEffectKey is None else [StringNode(sideEffectKey)],
            )
        )
        return self

    def groupCount(
        self, sideEffectKey: typing.Optional[str] = None
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "groupCount",
                [] if sideEffectKey is None else [StringNode(sideEffectKey)],
            )
        )
        return self

    def groupV3d0(
        self, sideEffectKey: typing.Optional[str] = None
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "groupV3d0",
                [] if sideEffectKey is None else [StringNode(sideEffectKey)],
            )
        )
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("has", [StringNode(propertyKey), StringNode(value)])
        )
        return self

    def hasId(self, id: str, *otherIds: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("hasId", [StringNode(v) for v in (id, *otherIds)])
        )
        return self

    def hasKey(self, label: str, *otherLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("hasKey", [StringNode(v) for v in (label, *otherLabels)])
        )
        return self

    def hasLabel(self, label: str, *otherLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("hasLabel", [StringNode(v) for v in (label, *otherLabels)])
        )
        return self

    def hasNot(self, propertyKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("hasNot", [StringNode(propertyKey)]))
        return self

    def hasValue(self, value: str, *otherValues: str) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode("hasValue", [StringNode(v) for v in (value, *otherValues)])
        )
        return self

    def id(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("id", []))
        return self

    def identity(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("identity", []))
        return self

    def in_(self, *edgeLabels: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("in", [StringNode(v) for v in edgeLabels]))
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

    def local(self, localTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("local", [AnyNode(localTraversal)]))
        return self

    def loops(self, loopName: typing.Optional[str] = None) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "loops",
                [] if loopName is None else [StringNode(loopName)],
            )
        )
        return self

    def map(self, mapTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("map", [AnyNode(mapTraversal)]))
        return self

    def match(self, *args: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("match", [AnyNode(v) for v in args]))
        return self

    def math(self, expression: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("math", [StringNode(expression)]))
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

    def none(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("none", []))
        return self

    def next(self, amount: int = 0) -> List:
        args = [] if amount == 0 else [IntegerNode(amount)]
        self.nodes.append(MethodCallNode("next", args))
        return List(self.nodes)

    def not_(self, notTraversal: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("not", [AnyNode(notTraversal)]))
        return self

    def option(self, traversalOption: "GraphTraversal") -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("option", [AnyNode(traversalOption)]))
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

    def peerPressure(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("peerPressure", []))
        return self

    def profile(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("profile", []))
        return self

    def project(
        self, projectKey: str, *otherProjectKeys: str
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "project", [StringNode(v) for v in (projectKey, *otherProjectKeys)]
            )
        )
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

    def sack(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("sack", []))
        return self

    def sample(self, amountToSample: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("sample", [IntegerNode(amountToSample)]))
        return self

    def select(self, selectKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("select", [StringNode(selectKey)]))
        return self

    def shortestPath(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("shortestPath", []))
        return self

    def simplePath(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("simplePath", []))
        return self

    def skip(self, skip: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("skip", [IntegerNode(skip)]))
        return self

    def subgraph(self, sideEffectKey: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("subgraph", [StringNode(sideEffectKey)]))
        return self

    def sum(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("sum", []))
        return self

    def tail(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("tail", []))
        return self

    def timeLimit(self, timeLimit: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("timeLimit", [IntegerNode(timeLimit)]))
        return self

    def times(self, maxLoops: int) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("times", [IntegerNode(maxLoops)]))
        return self

    def to(self, toStepLabel: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("to", [StringNode(toStepLabel)]))
        return self

    def tree(
        self, sideEffectKey: typing.Optional[str] = None
    ) -> "DefaultGraphTraversal":
        self.nodes.append(
            MethodCallNode(
                "tree",
                [] if sideEffectKey is None else [StringNode(sideEffectKey)],
            )
        )
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

    def unfold(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("unfold", []))
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

    def with_(self, key: str) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("with", [StringNode(key)]))
        return self

    def write(self) -> "DefaultGraphTraversal":
        self.nodes.append(MethodCallNode("write", []))
        return self
