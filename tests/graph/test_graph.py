class TestVariableAssignment:
    def test_case(self) -> None:
        from gremlin.graph import DefaultGraphTraversal, Variable

        g = DefaultGraphTraversal()
        assert g
        node = Variable("x").assignment(
            g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        )
        assert node
        assert (
            node.evaluate()
            == 'x=g.V().has("name","gremlin").out("knows").out("knows").values("name");'
        )
