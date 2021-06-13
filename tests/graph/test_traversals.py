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
    # Based on 3.5.0
    # http://tinkerpop.apache.org/javadocs/3.5.0/core/org/apache/tinkerpop/gremlin/process/traversal/dsl/graph/GraphTraversal.html

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
        g.asAdmin()
        g.barrier(1)
        g.both("")
        g.bothE("")
        g.bothV()
        g.branch(g.V())
        g.by(g, g)
        g.cap("")
        g.cap("", "")
        g.choose(g.V())
        g.coalesce(g.V())
        g.coin(0)
        g.connectedComponent()
        g.count()
        g.cyclicPath()
        g.dedup("")
        g.dedup("", "")
        g.drop()
        g.elementMap("")
        g.emit()
        g.filter(g.V())
        g.flatMap(g.V())
        g.fold()
        g.from_("")
        g.group()
        g.groupCount()
        g.groupCount("")
        g.has("key", "value")
        g.hasId("", "")
        g.hasKey("", "")
        g.hasLabel("")
        g.hasNot("")
        g.hasValue("", "")
        g.id()
        g.identity()
        g.in_("")
        g.in_("", "")
        g.index()
        g.inE("")
        g.inV()
        g.is_("")
        g.iterate()
        g.key()
        g.label()
        g.limit(0)
        g.local(g.V())
        g.loops()
        g.map(g.V())
        g.mapKeys()
        g.mapValues()
        g.match(g, g)
        g.max()
        g.mean()
        g.min()
        g.none()
        g.not_(g.V())
        g.option(g.V())
        g.or_(g.V())
        g.order(g)
        g.otherV()
        g.out("")
        g.outE()
        g.outV()
        g.pageRank()
        g.path()
        g.peerPressure()
        g.profile()
        g.project("")
        g.project("", "")
        g.properties("")
        g.propertyMap("")
        g.range(1, 2)
        g.repeat(g, g)
        g.sack()
        g.select("")
        g.sample(1)
        g.shortestPath()
        g.simplePath()
        g.subgraph("")
        g.store("")
        g.sum()
        g.tail()
        g.timeLimit(1)
        g.times(1)
        g.to("")
        g.tree()
        g.tree("")
        g.until(g, g)
        g.unfold()
        g.V()
        g.value()
        g.valueMap("")
        g.values("")
        g.where(g)
        g.with_("")
        g.write()


class TestDefaultGraphTraversal:
    @pytest.mark.parametrize(
        "method,test_labels,expected",
        [
            ("addE", ["arg"], 'g.V().addE("arg")'),
            ("addV", ["arg"], 'g.V().addV("arg")'),
            ("aggregate", ["arg"], 'g.V().aggregate("arg")'),
            ("and_", [], "g.V().and()"),
            ("as_", ["arg"], 'g.V().as("arg")'),
            ("as_", ["arg1", "arg2"], 'g.V().as("arg1","arg2")'),
            ("as_", ["arg1", "arg2", "arg3"], 'g.V().as("arg1","arg2","arg3")'),
            ("asAdmin", [], "g.V().asAdmin()"),
            ("barrier", [], "g.V().barrier()"),
            ("barrier", [1], "g.V().barrier(1)"),
            ("both", [], "g.V().both()"),
            ("both", ["arg"], 'g.V().both("arg")'),
            ("both", ["arg1", "arg2"], 'g.V().both("arg1","arg2")'),
            ("both", ["arg1", "arg2", "arg3"], 'g.V().both("arg1","arg2","arg3")'),
            ("bothE", ["arg"], 'g.V().bothE("arg")'),
            ("bothE", ["arg1", "arg2"], 'g.V().bothE("arg1","arg2")'),
            ("bothV", [], "g.V().bothV()"),
            # branch
            ("by", [], "g.V().by()"),
            ("by", ["arg"], 'g.V().by("arg")'),
            ("cap", ["arg"], 'g.V().cap("arg")'),
            ("cap", ["arg1", "arg2"], 'g.V().cap("arg1","arg2")'),
            ("cap", ["arg1", "arg2", "arg3"], 'g.V().cap("arg1","arg2","arg3")'),
            # choose
            # coalesce
            ("coin", [0], "g.V().coin(0)"),
            ("coin", [1], "g.V().coin(1)"),
            ("connectedComponent", [], "g.V().connectedComponent()"),
            ("count", [], "g.V().count()"),
            ("cyclicPath", [], "g.V().cyclicPath()"),
            ("dedup", ["arg"], 'g.V().dedup("arg")'),
            ("dedup", ["arg1", "arg2"], 'g.V().dedup("arg1","arg2")'),
            ("drop", [], "g.V().drop()"),
            ("elementMap", [], "g.V().elementMap()"),
            ("elementMap", ["arg"], 'g.V().elementMap("arg")'),
            ("elementMap", ["arg1", "arg2"], 'g.V().elementMap("arg1","arg2")'),
            ("emit", [], "g.V().emit()"),
            # filter
            # flatMap
            ("fold", [], "g.V().fold()"),
            ("from_", ["arg"], 'g.V().from("arg")'),
            ("group", [], "g.V().group()"),
            ("group", ["arg"], 'g.V().group("arg")'),
            ("groupCount", [], "g.V().groupCount()"),
            ("groupCount", ["arg"], 'g.V().groupCount("arg")'),
            ("has", ["arg"], 'g.V().has("arg")'),
            ("hasId", ["arg"], 'g.V().hasId("arg")'),
            ("hasId", ["arg1", "arg2"], 'g.V().hasId("arg1","arg2")'),
            ("hasKey", ["arg"], 'g.V().hasKey("arg")'),
            ("hasKey", ["arg1", "arg2"], 'g.V().hasKey("arg1","arg2")'),
            ("hasLabel", ["arg"], 'g.V().hasLabel("arg")'),
            ("hasLabel", ["arg1", "arg2"], 'g.V().hasLabel("arg1","arg2")'),
            ("hasNot", ["arg"], 'g.V().hasNot("arg")'),
            ("hasValue", ["arg"], 'g.V().hasValue("arg")'),
            ("hasValue", ["arg1", "arg2"], 'g.V().hasValue("arg1","arg2")'),
            ("id", [], "g.V().id()"),
            ("identity", [], "g.V().identity()"),
            ("in_", ["arg"], 'g.V().in("arg")'),
            ("in_", ["arg1", "arg2"], 'g.V().in("arg1","arg2")'),
            ("index", [], "g.V().index()"),  # ???
            ("inE", [], "g.V().inE()"),
            ("inE", ["arg"], 'g.V().inE("arg")'),
            ("inE", ["arg1", "arg2"], 'g.V().inE("arg1","arg2")'),
            # injection
            ("inV", [], "g.V().inV()"),
            ("iterate", [], "g.V().iterate()"),
            ("key", [], "g.V().key()"),
            ("label", [], "g.V().label()"),
            ("limit", [0], "g.V().limit(0)"),
            ("loops", [], "g.V().loops()"),
            ("mapKeys", [], "g.V().mapKeys()"),  # Deprecated
            ("mapValues", [], "g.V().mapValues()"),  # Deprecated
            ("max", [], "g.V().max()"),
            ("mean", [], "g.V().mean()"),
            ("min", [], "g.V().min()"),
            ("next", [], "g.V().next()"),
            ("next", [1], "g.V().next(1)"),
            ("none", [], "g.V().none()"),
            ("order", [], "g.V().order()"),
            ("otherV", [], "g.V().otherV()"),
            ("out", [], "g.V().out()"),
            ("out", ["arg"], 'g.V().out("arg")'),
            ("out", ["arg1", "arg2"], 'g.V().out("arg1","arg2")'),
            ("outE", [], "g.V().outE()"),
            ("outE", ["arg"], 'g.V().outE("arg")'),
            ("outE", ["arg1", "arg2"], 'g.V().outE("arg1","arg2")'),
            ("outV", [], "g.V().outV()"),
            ("pageRank", [], "g.V().pageRank()"),
            ("pageRank", [1], "g.V().pageRank(1)"),
            ("path", [], "g.V().path()"),
            ("peerPressure", [], "g.V().peerPressure()"),
            ("profile", [], "g.V().profile()"),
            ("project", ["arg"], 'g.V().project("arg")'),
            ("project", ["arg1", "arg2"], 'g.V().project("arg1","arg2")'),
            ("properties", ["arg"], 'g.V().properties("arg")'),
            ("properties", ["arg1", "arg2"], 'g.V().properties("arg1","arg2")'),
            ("propertyMap", ["arg"], 'g.V().propertyMap("arg")'),
            ("range", [1, 2], "g.V().range(1,2)"),
            ("sack", [], "g.V().sack()"),
            ("sample", [1], "g.V().sample(1)"),
            ("select", ["arg"], 'g.V().select("arg")'),
            ("shortestPath", [], "g.V().shortestPath()"),
            ("simplePath", [], "g.V().simplePath()"),
            ("store", ["arg"], 'g.V().store("arg")'),
            ("subgraph", ["arg1"], 'g.V().subgraph("arg1")'),
            ("sum", [], "g.V().sum()"),
            ("tail", [], "g.V().tail()"),
            ("tail", [1], "g.V().tail(1)"),
            ("timeLimit", [0], "g.V().timeLimit(0)"),
            ("timeLimit", [1], "g.V().timeLimit(1)"),
            ("times", [0], "g.V().times(0)"),
            ("times", [1], "g.V().times(1)"),
            ("to", [""], 'g.V().to("")'),
            ("to", ["arg"], 'g.V().to("arg")'),
            ("toList", [], "g.V().toList()"),  # ???
            ("toSet", [], "g.V().toSet()"),  # ???
            ("tree", [], "g.V().tree()"),
            ("tree", ["arg"], 'g.V().tree("arg")'),
            ("unfold", [], "g.V().unfold()"),
            ("value", [], "g.V().value()"),
            ("valueMap", [], "g.V().valueMap()"),
            ("valueMap", ["arg"], 'g.V().valueMap("arg")'),
            ("values", ["arg"], 'g.V().values("arg")'),
            ("with_", ["arg"], 'g.V().with("arg")'),  # ???
            ("write", [], "g.V().write()"),  # ???
        ],
    )
    def test_V_methods(
        self, method: str, test_labels: typing.List[str], expected: str
    ) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        node = getattr(g.V(), method)(*test_labels)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "method,expected",
        [
            ("and_", "g.V().and(g.V())"),
            ("branch", "g.V().branch(g.V())"),
            ("choose", "g.V().choose(g.V())"),
            ("coalesce", "g.V().coalesce(g.V())"),
            ("filter", "g.V().filter(g.V())"),
            ("flatMap", "g.V().flatMap(g.V())"),
            ("local", "g.V().local(g.V())"),
            ("map", "g.V().map(g.V())"),
            ("not_", "g.V().not(g.V())"),
            ("option", "g.V().option(g.V())"),
            ("or_", "g.V().or(g.V())"),
        ],
    )
    def test_V_methods_with_V(self, method: str, expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        node = getattr(g.V(), method)(g.V())
        assert node
        assert node.evaluate() == expected


class TestDefaultGraphTraversalUsecases:
    def test_case1(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        node = g.V().has("name", "gremlin").out("knows").out("knows").values("name")
        assert node
        assert (
            node.evaluate()
            == 'g.V().has("name","gremlin").out("knows").out("knows").values("name")'
        )

    def test_case2(self) -> None:
        from gremlin.graph import DefaultGraphTraversal, as_

        g = DefaultGraphTraversal()
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
