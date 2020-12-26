import typing
import pytest


class TestNode:
    def test_instantiate(self) -> None:
        from gremlin.nodes import Node

        node = Node()
        assert node
        node.evaluate()


class TestMethodCallNode:
    @pytest.mark.parametrize("type,arguments", [("has", ["name", "gremlin"])])
    def test_instantiate(self, type: str, arguments: typing.List[str]) -> None:
        from gremlin.nodes import MethodCallNode, StringNode

        node = MethodCallNode(type, [StringNode(v) for v in arguments])
        assert node
        assert node.evaluate() == '.has("name","gremlin")'
