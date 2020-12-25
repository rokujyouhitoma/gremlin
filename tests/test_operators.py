import typing
import pytest


class TestFunctionOperator:
    @pytest.mark.parametrize("type,arguments", [("has", ["name", "gremlin"])])
    def test_instantiate(self, type: str, arguments: typing.List[str]) -> None:
        from something.operators import FunctionOperator

        operator = FunctionOperator(type, arguments)
        assert operator
        assert operator.evaluate() == '.has("name","gremlin")'
