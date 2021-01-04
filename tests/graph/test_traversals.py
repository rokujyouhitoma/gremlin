import typing

import pytest


class TestTraversal:
    def test_interfaces(self) -> None:
        from gremlin.graph import Traversal

        g = Traversal()
        assert g
        g.iterate()
        g.next(1)
        g.none()
        g.toList()
        g.toSet()


class TestGraphTraversal:
    def test_interfaces(self) -> None:
        from gremlin.graph import GraphTraversal

        g = GraphTraversal()
        assert g
        g.addE("")
        g.addE(g.V())
        g.addV("")
        g.aggregate("")
        g.and_(g, g)
        g.as_("")
        g.both("")
        g.bothE("")
        g.bothV()
        g.by(g, g)
        g.count()
        g.drop()
        g.elementMap("")
        g.groupCount()
        g.has("key", "value")
        g.hasLabel("")
        g.id()
        g.in_("")
        g.index()
        g.inE("")
        g.inV()
        g.is_("")
        g.iterate()
        g.key()
        g.label()
        g.limit(0)
        g.match(g, g)
        g.max()
        g.mean()
        g.min()
        g.not_(g.V())
        g.or_(g.V())
        g.order(g)
        g.otherV()
        g.out("")
        g.outE()
        g.outV()
        g.pageRank()
        g.path()
        g.repeat(g, g)
        g.select("")
        g.until(g, g)
        g.V()
        g.value()
        g.valueMap("")
        g.values("")
        g.where(g)


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

    def test_addE2(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.addE(g.V())
        assert node
        assert node.evaluate() == "g.addE(g.V())"

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

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().bothV()"),
        ],
    )
    def test_bothV(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().bothV(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().drop()"),
        ],
    )
    def test_drop(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().drop(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().elementMap()"),
            (["arg"], 'g.V().elementMap("arg")'),
            (["arg1", "arg2"], 'g.V().elementMap("arg1","arg2")'),
        ],
    )
    def test_elementMap(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().elementMap(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().hasLabel("arg")'),
            (["arg1", "arg2"], 'g.V().hasLabel("arg1","arg2")'),
        ],
    )
    def test_hasLabel(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().hasLabel(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().id()"),
        ],
    )
    def test_id(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().id(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().index()"),
        ],
    )
    def test_index(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().index(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().inE()"),
            (["arg"], 'g.V().inE("arg")'),
            (["arg1", "arg2"], 'g.V().inE("arg1","arg2")'),
        ],
    )
    def test_inE(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().inE(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().inV()"),
        ],
    )
    def test_inV(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().inV(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().iterate()"),
        ],
    )
    def test_iterate(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().iterate(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().key()"),
        ],
    )
    def test_key(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().key(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().label()"),
        ],
    )
    def test_label(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().label(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().max()"),
        ],
    )
    def test_max(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().max(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().mean()"),
        ],
    )
    def test_mean(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().mean(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().min()"),
        ],
    )
    def test_min(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().min(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().next()"),
            ([1], "g.V().next(1)"),
        ],
    )
    def test_next(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().next(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().none()"),
        ],
    )
    def test_none(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().none(*test_args)
        assert node
        assert node.evaluate() == expected

    def test_not_(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().not_(g.V())
        assert node
        assert node.evaluate() == "g.V().not(g.V())"

    def test_or_(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().or_(g.V())
        assert node
        assert node.evaluate() == "g.V().or(g.V())"

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().otherV()"),
        ],
    )
    def test_otherV(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().otherV(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().out()"),
            (["arg"], 'g.V().out("arg")'),
            (["arg1", "arg2"], 'g.V().out("arg1","arg2")'),
        ],
    )
    def test_out(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().out(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().outE()"),
            (["arg"], 'g.V().outE("arg")'),
            (["arg1", "arg2"], 'g.V().outE("arg1","arg2")'),
        ],
    )
    def test_outE(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().outE(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().outV()"),
        ],
    )
    def test_outV(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().outV(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().toList()"),
        ],
    )
    def test_toList(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().toList(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().toSet()"),
        ],
    )
    def test_toSet(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().toSet(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().value()"),
        ],
    )
    def test_value(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().value(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().valueMap()"),
        ],
    )
    def test_valueMap(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().valueMap(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().values("arg")'),
        ],
    )
    def test_values(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().values(*test_args)
        assert node
        assert node.evaluate() == expected


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
