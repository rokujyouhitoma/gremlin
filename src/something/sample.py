import typing

from something.operators import FunctionOperator, Operator, StringOperator


class GraphTraversal(Operator):
    operators: typing.List[Operator] = [StringOperator("g")]

    def generate(self) -> typing.Generator[Operator, None, None]:
        for operator in self.operators:
            yield operator

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in self.generate())

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

    def generate(self) -> typing.Generator[Operator, None, None]:
        for operator in self.operators:
            yield operator

    def evaluate(self) -> str:
        return "".join(operator.evaluate() for operator in (self.generate()))

    def assignment(self, g: GraphTraversal) -> "Variable":
        # TODO:
        self.operators.append(StringOperator(self.name))
        self.operators.append(StringOperator("="))
        self.operators.append(g)
        self.operators.append(StringOperator(";"))
        return self
