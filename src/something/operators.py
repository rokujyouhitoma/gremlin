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
