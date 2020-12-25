import typing
from dataclasses import dataclass


class Node:
    def evaluate(self) -> str:
        pass


@dataclass
class StringNode(Node):
    value: str

    def evaluate(self) -> str:
        return self.value


@dataclass
class FunctionNode(Node):
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
class IdentifierNode(StringNode):
    pass


@dataclass
class EqualNode(StringNode):
    value: str = "="


@dataclass
class gNode(StringNode):
    value: str = "g"


@dataclass
class SemicolonNode(StringNode):
    value: str = ";"


class MultipleNode(Node):
    nodes: typing.List[Node] = []

    def generate(self) -> typing.Generator[Node, None, None]:
        for node in self.nodes:
            yield node

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in self.generate())
