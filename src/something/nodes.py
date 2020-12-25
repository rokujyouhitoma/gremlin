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
class IdentifierNode(StringNode):
    pass


@dataclass
class DotNode(StringNode):
    value: str = "."


@dataclass
class EqualNode(StringNode):
    value: str = "="


@dataclass
class gNode(StringNode):
    value: str = "g"


@dataclass
class SemicolonNode(StringNode):
    value: str = ";"


@dataclass
class OpenBlacketNode(StringNode):
    value: str = "("


@dataclass
class CloseBlacketNode(StringNode):
    value: str = ")"


class MultipleNode(Node):
    nodes: typing.List[Node] = []

    def generate(self) -> typing.Generator[Node, None, None]:
        for node in self.nodes:
            yield node

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in self.generate())


@dataclass
class CallNameNode(StringNode):
    pass


@dataclass
class ArgumentListNode(Node):
    argument_list: typing.List[typing.Any]

    def evaluate(self) -> str:
        if not len(self.argument_list):
            return ""
        return '"' + '","'.join(self.argument_list) + '"'


class CallNode(MultipleNode):
    def __init__(
        self, call_name_node: CallNameNode, argument_list_node: ArgumentListNode
    ):
        self.nodes = [
            call_name_node,
            OpenBlacketNode(),
            argument_list_node,
            CloseBlacketNode(),
        ]


class MethodCallNode(MultipleNode):
    def __init__(self, method_name: str, argument_list: typing.List[typing.Any]):
        self.nodes = [
            DotNode(),
            CallNode(CallNameNode(method_name), ArgumentListNode(argument_list)),
        ]


class AssignmentStatement(MultipleNode):
    def __init__(self, identifier: IdentifierNode, node: Node):
        self.nodes = [
            identifier,
            EqualNode(),
            node,
            SemicolonNode(),
        ]
