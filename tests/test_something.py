class TestSomething:
    # See: https://tinkerpop.apache.org/

    def test_case1(self) -> None:
        from something.nodes import gNode
        from something.sample import GraphTraversal, Variable

        g = GraphTraversal([gNode()])
        assert g
        node = Variable("x").assignment(
            g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        )
        assert node
        assert (
            node.evaluate()
            == 'x=g.V().has("name","gremlin").out("knows").out("knows").values("name");'
        )

    def test_case2(self) -> None:
        from something.nodes import gNode
        from something.sample import GraphTraversal, as_

        g = GraphTraversal([gNode()])
        assert g
        node = (
            g.V()
            .match(
                as_("a").out("knows").as_("b"),
                as_("a").out("created").as_("c"),
                as_("b").out("created").as_("c"),
                as_("c").in_("created").count().is_(2),
            )
            .select("c")
            .by("name")
        )
        assert node
        assert (
            node.evaluate() == "g.V().match("
            'as("a").out("knows").as("b"),'
            'as("a").out("created").as("c"),'
            'as("b").out("created").as("c"),'
            'as("c").in("created").count().is(2)'
            ').select("c").by("name")'
        )
