from dataclasses import dataclass

from gremlin.nodes import AssignmentStatement, IdentifierNode, MultipleNode, Node


@dataclass
class Variable(MultipleNode):
    name: str

    def assignment(self, node: Node) -> "Variable":
        self.nodes.append(AssignmentStatement(IdentifierNode(self.name), node))
        return self
