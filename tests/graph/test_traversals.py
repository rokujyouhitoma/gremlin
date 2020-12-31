import typing

import pytest


class TestGraphTraversal:
    def test_interfaces(self) -> None:
        from gremlin.graph import GraphTraversal

        g = GraphTraversal()
        assert g
        g.addE("")
        g.addV("")
        g.aggregate("")
        g.and_(g, g)
        g.as_("")
        g.both("")
        g.bothE("")
        g.by(g, g)
        g.count()
        g.groupCount()
        g.has("key", "value")
        g.hasLabel("")
        g.limit(0)
        g.in_("")
        g.is_("")
        g.next()
        g.not_(g, g)
        g.match(g, g)
        g.mean()
        g.pageRank()
        g.out("")
        g.order(g, g)
        g.path()
        g.repeat(g, g)
        g.until(g, g)
        g.select("")
        g.V()
        g.values("")
        g.where(g, g)


class TestDefaultGraphTraversal:
    @pytest.mark.parametrize(
        "test_label,expected",
        [
            ("", 'g.addE("")'),
            ("test", 'g.addE("test")'),
        ],
    )
    def test_addE(self, test_label: str, expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.addE(test_label)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_label,expected",
        [
            ("", 'g.addV("")'),
            ("test", 'g.addV("test")'),
        ],
    )
    def test_addV(self, test_label: str, expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.addV(test_label)
        assert node
        assert node.evaluate() == expected

    def test_add_(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().and_()
        assert node
        assert node.evaluate() == "g.V().and()"

    @pytest.mark.parametrize(
        "test_labels,expected",
        [
            (["arg1"], 'g.V().as("arg1")'),
            (["arg1", "arg2"], 'g.V().as("arg1","arg2")'),
        ],
    )
    def test_as_(self, test_labels: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().as_(*test_labels)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_labels,expected",
        [
            ([], "g.V().both()"),
            (["arg1"], 'g.V().both("arg1")'),
            (["arg1", "arg2"], 'g.V().both("arg1","arg2")'),
        ],
    )
    def test_both(self, test_labels: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().both(*test_labels)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_labels,expected",
        [
            ([], "g.V().bothE()"),
            (["arg1"], 'g.V().bothE("arg1")'),
            (["arg1", "arg2"], 'g.V().bothE("arg1","arg2")'),
        ],
    )
    def test_bothE(self, test_labels: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().bothE(*test_labels)
        assert node
        assert node.evaluate() == expected

    def test_not_(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().not_()
        assert node
        assert node.evaluate() == "g.V().not()"


class TestDefaultGraphTraversalUsecases:
    def test_case1(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","gremlin").out("knows").out("knows").values("name")'
        )

    def test_case2(self) -> None:
        from gremlin.graph import DefaultGraphTraversal, as_

        g = DefaultGraphTraversal()
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
        from gremlin.graph import DefaultGraphTraversal, in_, has

        g = DefaultGraphTraversal()
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
        from gremlin.graph import DefaultGraphTraversal, neq

        g = DefaultGraphTraversal()
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
        from gremlin.graph import (
            DefaultGraphTraversal,
            not_,
            within,
            local,
            values,
            desc,
        )

        g = DefaultGraphTraversal()
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
        from gremlin.graph import DefaultGraphTraversal, outE, desc

        g = DefaultGraphTraversal()
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
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
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
