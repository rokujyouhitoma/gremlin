class TestGremlin:
    # Language sample by Apache TinkerPop official site.
    # See: https://tinkerpop.apache.org/

    def test_case1(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal

        g = GraphTraversal([gNode()])
        assert g
        node = g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","gremlin").out("knows").out("knows").values("name")'
        )

    def test_case2(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, as_

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

    def test_case3(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, in_, has

        g = GraphTraversal([gNode()])
        assert g
        node = (
            g.V()
            .has("name", "gremlin")
            .repeat(in_("manages"))
            .until(has("title", "ceo"))
            .path()
            .by("name")
        )
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","gremlin").repeat(in("manages")).until(has("title","ceo")).path().by("name")'
        )

    def test_case4(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, neq

        g = GraphTraversal([gNode()])
        assert g
        node = (
            g.V()
            .has("name", "gremlin")
            .as_("a")
            .out("created")
            .in_("created")
            .where(neq("a"))
            .groupCount()
            .by("title")
        )
        assert node
        assert (
            node.evaluate() == 'g.V().has("name","gremlin").as("a")'
            '.out("created").in("created").where(neq("a")).groupCount().by("title")'
        )

    def test_case5(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, not_, within, local, values, desc

        g = GraphTraversal([gNode()])
        assert g
        node = (
            g.V()
            .has("name", "gremlin")
            .out("bought")
            .aggregate("stash")
            .in_("bought")
            .out("bought")
            .where(not_(within("stash")))
            .groupCount()
            .order(local)
            .by(values, desc)
        )
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","gremlin").out("bought").aggregate("stash")'
            '.in("bought").out("bought")'
            '.where(not(within("stash")))'
            ".groupCount().order(local).by(values,desc)"
        )

    def test_case6(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, outE, desc

        g = GraphTraversal([gNode()])
        assert g
        node = (
            g.V()
            .hasLabel("person")
            .pageRank()
            .by("friendRank")
            .by(outE("knows"))
            .order()
            .by("friendRank", desc)
            .limit(10)
        )
        assert node
        assert (
            node.evaluate()
            == 'g.V().hasLabel("person").pageRank().by("friendRank").by(outE("knows"))'
            '.order().by("friendRank",desc).limit(10)'
        )

    def test_case7(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal

        g = GraphTraversal([gNode()])
        assert g
        name = "name1"
        property = "property1"
        node = (
            g.V()
            .has("name", name)
            .out("knows")
            .out("created")
            .values(property)
            .mean()
            .next()
        )
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","name1").out("knows").out("created").values("property1").mean().next()'
        )


class TestVariableAssignment:
    def test_case(self) -> None:
        from gremlin.nodes import gNode
        from gremlin.graph import GraphTraversal, Variable

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
