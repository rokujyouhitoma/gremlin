import typing
from dataclasses import dataclass


class Node:
    def evaluate(self) -> str:
        pass


@dataclass
class ValueNode(Node):
    value: str

    def evaluate(self) -> str:
        return self.value


@dataclass
class StringNode(Node):
    value: str

    def evaluate(self) -> str:
        return f'"{self.value}"'


@dataclass
class IntegerNode(Node):
    value: int

    def evaluate(self) -> str:
        return str(self.value)


@dataclass
class IdentifierNode(ValueNode):
    pass


@dataclass
class DotNode(ValueNode):
    value: str = "."


@dataclass
class EqualNode(ValueNode):
    value: str = "="


@dataclass
class gNode(ValueNode):
    value: str = "g"


@dataclass
class SemicolonNode(ValueNode):
    value: str = ";"


@dataclass
class OpenBlacketNode(ValueNode):
    value: str = "("


@dataclass
class CloseBlacketNode(ValueNode):
    value: str = ")"


class MultipleNode(Node):
    nodes: typing.List[Node] = []

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in self.nodes)


@dataclass
class CallNameNode(ValueNode):
    pass


@dataclass
class ArgumentListNode(Node):
    argument_list: typing.Sequence[typing.Any]

    def evaluate(self) -> str:
        if not len(self.argument_list):
            return ""
        return ",".join([argument.evaluate() for argument in self.argument_list])


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
    def __init__(self, method_name: str, argument_list: typing.Sequence[typing.Any]):
        self.nodes = [
            DotNode(),
            CallNode(CallNameNode(method_name), ArgumentListNode(argument_list)),
        ]


class MethodCallNodeArgumentsNode(MultipleNode):
    def __init__(self, method_name: str, argument_list: typing.Sequence[Node]):
        self.nodes = [
            DotNode(),
            CallNameNode(method_name),
        ]
        self.nodes.append(OpenBlacketNode())
        for index, node in enumerate(argument_list):
            if index != 0:
                self.nodes.append(ValueNode(","))
            self.nodes.append(node)
        self.nodes.append(CloseBlacketNode())


class AssignmentStatement(MultipleNode):
    def __init__(self, identifier: IdentifierNode, node: Node):
        self.nodes = [
            identifier,
            EqualNode(),
            node,
            SemicolonNode(),
        ]
