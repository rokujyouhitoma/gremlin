import typing
import pytest


class TestMethodCallNode:
    @pytest.mark.parametrize("type,arguments", [("has", ["name", "gremlin"])])
    def test_instantiate(self, type: str, arguments: typing.List[str]) -> None:
        from something.nodes import MethodCallNode

        node = MethodCallNode(type, arguments)
        assert node
        assert node.evaluate() == '.has("name","gremlin")'
