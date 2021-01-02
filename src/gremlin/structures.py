import typing
from dataclasses import dataclass, field

from .nodes import Node


@dataclass
class List(Node):
    nodes: typing.List[Node] = field(default_factory=list)

    def evaluate(self) -> str:
        return "".join(node.evaluate() for node in self.nodes)
