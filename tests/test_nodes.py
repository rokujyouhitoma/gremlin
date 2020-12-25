import typing
import pytest


class TestFunctionNode:
    @pytest.mark.parametrize("type,arguments", [("has", ["name", "gremlin"])])
    def test_instantiate(self, type: str, arguments: typing.List[str]) -> None:
        from something.nodes import FunctionNode

        node = FunctionNode(type, arguments)
        assert node
        assert node.evaluate() == '.has("name","gremlin")'
