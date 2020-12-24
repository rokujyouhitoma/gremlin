"""
case1:
variable = globalContext.someOperation();

=>
Variable("label").assignment(globalContext.someOperation())

=>
Variable("label").assignment(g.addE("label"))
"""

from dataclasses import dataclass, field
import typing


@dataclass
class Command:
    type: str
    arguments: list


class Operator:
    commands: typing.List[Command] = []


class GraphTraversal(Operator):
    """
    see: http://tinkerpop.apache.org/javadocs/current/full/org/apache/tinkerpop/gremlin/process/traversal/dsl/graph/GraphTraversal.html
    """
    commands: typing.List[Command] = [Command("g", [])]

    def __repr__(self):
        return f"<GraphTraversal:{str(self.commands)}>"

    def addE(self, edgeLabel: str):
        self.commands.append(Command("addE", [edgeLabel]))
        return self

    def addV(self, vertexLabel: str = ""):
        self.commands.append(Command("addV", [vertexLabel]))
        return self

    def has(self, propertyKey: str, value: typing.Any):
        self.commands.append(Command("has", [propertyKey, value]))
        return self

    def out(self, edgeLabel: str):
        self.commands.append(Command("out", [edgeLabel]))
        return self

    def V(self):
        self.commands.append(Command("V", []))
        return self

    def values(self, propertyKey: str):
        self.commands.append(Command("values", [propertyKey]))
        return self


class Variable(Operator):
    name: str
    commands: typing.List[Command] = []

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Variable:{str(self.commands)}>"

    def assignment(self, g: GraphTraversal):
        self.commands.append(Command("variable", [self.name, g]))
        return self


@dataclass
class Context(Operator):
    commands: typing.List[Command] = field(default_factory=list)


g = GraphTraversal()
context = Context([
    Variable("x").assignment(g.V().has("name","gremlin").out("knows").out("knows").values("name"))
])

import pprint
pprint.pprint(context)
