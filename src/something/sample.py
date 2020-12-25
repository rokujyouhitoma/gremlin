import typing

from something.nodes import (
    EqualNode,
    FunctionNode,
    IdentifierNode,
    Node,
    SemicolonNode,
    gNode,
)


class GraphTraversal(Node):
    operators: typing.List[Node] = [gNode()]

    def generate(self) -> typing.Generator[Node, None, None]:
        for operator in self.operators:
            yield operator

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in self.generate())

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.operators.append(FunctionNode("addE", [edgeLabel]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.operators.append(FunctionNode("addV", [vertexLabel]))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.operators.append(FunctionNode("has", [propertyKey, value]))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.operators.append(FunctionNode("out", [edgeLabel]))
        return self

    def V(self) -> "GraphTraversal":
        self.operators.append(FunctionNode("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.operators.append(FunctionNode("values", [propertyKey]))
        return self


class Variable(Node):
    name: str
    operators: typing.List[Node] = []

    def __init__(self, name: str):
        self.name = name

    def generate(self) -> typing.Generator[Node, None, None]:
        for operator in self.operators:
            yield operator

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in (self.generate()))

    def assignment(self, g: GraphTraversal) -> "Variable":
        # TODO:
        self.operators.append(IdentifierNode(self.name))
        self.operators.append(EqualNode())
        self.operators.append(g)
        self.operators.append(SemicolonNode())
        return self
