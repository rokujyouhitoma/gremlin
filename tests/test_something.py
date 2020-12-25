class TestSomething:
    def test_(self) -> None:
        # See: https://tinkerpop.apache.org/
        from something.sample import GraphTraversal, Variable

        g = GraphTraversal()
        assert g
        node = Variable("x").assignment(
            g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        )
        assert node
        assert (
            node.evaluate()
            == 'x=g.V().has("name","gremlin").out("knows").out("knows").values("name");'
        )
