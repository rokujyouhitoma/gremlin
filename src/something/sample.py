import typing
from dataclasses import dataclass


class Operator:
    def evaluate(self) -> str:
        pass


@dataclass
class StringOperator(Operator):
    value: str

    def evaluate(self) -> str:
        return self.value


@dataclass
class FunctionOperator(Operator):
    type: str
    arguments: typing.List[typing.Any]

    def evaluate(self) -> str:
        type = self.type
        if len(self.arguments):
            arguments = '","'.join(self.arguments)
            return f'.{type}("{arguments}")'
        else:
            return f".{type}()"


@dataclass
class GraphTraversalOperator(Operator):
    name: str

    def evaluate(self) -> str:
        return self.name


class GraphTraversal(Operator):
    operators: typing.List[Operator] = [GraphTraversalOperator("g")]

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in (self.operators))

    # def __repr__(self) -> str:
    #    return f"<GraphTraversal:{str(self.operators)}>"

    def addE(self, edgeLabel: str) -> "GraphTraversal":
        self.operators.append(FunctionOperator("addE", [edgeLabel]))
        return self

    def addV(self, vertexLabel: str = "") -> "GraphTraversal":
        self.operators.append(FunctionOperator("addV", [vertexLabel]))
        return self

    def has(self, propertyKey: str, value: typing.Any) -> "GraphTraversal":
        self.operators.append(FunctionOperator("has", [propertyKey, value]))
        return self

    def out(self, edgeLabel: str) -> "GraphTraversal":
        self.operators.append(FunctionOperator("out", [edgeLabel]))
        return self

    def V(self) -> "GraphTraversal":
        self.operators.append(FunctionOperator("V", []))
        return self

    def values(self, propertyKey: str) -> "GraphTraversal":
        self.operators.append(FunctionOperator("values", [propertyKey]))
        return self


class Variable(Operator):
    name: str
    operators: typing.List[Operator] = []

    def __init__(self, name: str):
        self.name = name

    # def __repr__(self) -> str:
    #    return f"<Variable:{str(self.operators)}>"

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in (self.operators))

    def assignment(self, g: GraphTraversal) -> "Variable":
        # TODO:
        self.operators.append(StringOperator(self.name))
        self.operators.append(StringOperator("="))
        self.operators.append(g)
        self.operators.append(StringOperator(";"))
        return self
