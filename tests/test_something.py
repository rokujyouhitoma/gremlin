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
