import typing

from gremlin.graph.traversals import GraphTraversal
from gremlin.nodes import CallNode, StringNode, ValueNode


def as_(stepLabel: str) -> GraphTraversal:
    return GraphTraversal([CallNode("as", [StringNode(stepLabel)])])


desc = GraphTraversal([ValueNode("desc")])


def has(propertyKey: str, value: typing.Any) -> GraphTraversal:
    return GraphTraversal(
        [CallNode("has", [StringNode(propertyKey), StringNode(value)])]
    )


local = GraphTraversal([ValueNode("local")])


def not_(*args: "GraphTraversal") -> GraphTraversal:
    return GraphTraversal([CallNode("not", args)])


def in_(edgeLabel: str) -> GraphTraversal:
    return GraphTraversal([CallNode("in", [StringNode(edgeLabel)])])


def neq(value: str) -> GraphTraversal:
    return GraphTraversal([CallNode("neq", [StringNode(value)])])


def outE(value: str) -> GraphTraversal:
    return GraphTraversal([CallNode("outE", [StringNode(value)])])


def within(label: str) -> GraphTraversal:
    return GraphTraversal([CallNode("within", [StringNode(label)])])


values = GraphTraversal([ValueNode("values")])
