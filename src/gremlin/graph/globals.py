import typing

from gremlin.graph.traversals import DefaultGraphTraversal, GraphTraversal
from gremlin.nodes import AnyNode, CallNode, StringNode, ValueNode


def as_(stepLabel: str) -> GraphTraversal:
    return DefaultGraphTraversal([CallNode("as", [StringNode(stepLabel)])])


desc = DefaultGraphTraversal([ValueNode("desc")])


def has(propertyKey: str, value: typing.Any) -> GraphTraversal:
    return DefaultGraphTraversal(
        [CallNode("has", [StringNode(propertyKey), StringNode(value)])]
    )


local = DefaultGraphTraversal([ValueNode("local")])


def not_(*args: "GraphTraversal") -> GraphTraversal:
    argument_list = [AnyNode(v) for v in args]
    return DefaultGraphTraversal([CallNode("not", argument_list)])


def in_(edgeLabel: str) -> GraphTraversal:
    return DefaultGraphTraversal([CallNode("in", [StringNode(edgeLabel)])])


def neq(value: str) -> GraphTraversal:
    return DefaultGraphTraversal([CallNode("neq", [StringNode(value)])])


def outE(value: str) -> GraphTraversal:
    return DefaultGraphTraversal([CallNode("outE", [StringNode(value)])])


def within(label: str) -> GraphTraversal:
    return DefaultGraphTraversal([CallNode("within", [StringNode(label)])])


values = DefaultGraphTraversal([ValueNode("values")])
