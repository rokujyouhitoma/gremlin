import pytest


class TestSomething:
    def test_(self):
        # See: https://tinkerpop.apache.org/
        from something.sample import GraphTraversal, Variable
        g = GraphTraversal()
        assert g
        operator = Variable("x").assignment(
            g.V().has("name", "gremlin").out("knows").out("knows").values("name"))
        assert operator
        assert operator.evaluate() == 'x=g.V().has("name","gremlin").out("knows").out("knows").values("name");'


class TestFunctionOperator:
    @pytest.mark.parametrize(
        "type,arguments", [
            ("has", ["name", "gremlin"])
        ]
    )
    def test_instantiate(self, type, arguments):
        from something.sample import FunctionOperator
        operator = FunctionOperator(type, arguments)
        assert operator
        assert operator.evaluate() == '.has("name","gremlin")'
