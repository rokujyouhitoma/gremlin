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
        g.loops("")
        g.map(g.V())
        g.match(g, g)
        g.math("")
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
        g.repeat(g, g)
        g.sack()
        g.select("")
        g.sample(1)
        g.shortestPath()
        g.simplePath()
        g.skip(1)
        g.subgraph("")
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
            ("addE", [""], 'g.addE("")'),
            ("addE", ["test"], 'g.addE("test")'),
            ("addE", ["test"], 'g.addE("test")'),
            ("addV", [], "g.addV()"),
            ("addV", [""], 'g.addV("")'),
            ("addV", ["test"], 'g.addV("test")'),
        ],
    )
    def test_methods(
        self, method: str, test_labels: typing.List[str], expected: str
    ) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = getattr(g, method)(*test_labels)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "method,expected",
        [
            ("addE", "g.addE(g.V())"),
        ],
    )
    def test_methods2(self, method: str, expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = getattr(g, method)(g.V())
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
        "test_args,expected",
        [
            ([], "g.V().asAdmin()"),
        ],
    )
    def test_asAdmin(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().asAdmin(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().barrier()"),
            ([1], "g.V().barrier(1)"),
        ],
    )
    def test_barrier(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().barrier(*test_args)
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
            # TODO
            ([], "g.V().branch(g.V())"),
        ],
    )
    def test_branch(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().branch(g.V())
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([""], 'g.V().cap("")'),
            (["arg"], 'g.V().cap("arg")'),
            (["arg1", "arg2"], 'g.V().cap("arg1","arg2")'),
        ],
    )
    def test_cap(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().cap(*test_args)
        assert node
        assert node.evaluate() == expected

    def test_choose(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().choose(g.V())
        assert node
        assert node.evaluate() == "g.V().choose(g.V())"

    def test_coalesce(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().coalesce(g.V())
        assert node
        assert node.evaluate() == "g.V().coalesce(g.V())"

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([0], "g.V().coin(0)"),
            ([1], "g.V().coin(1)"),
        ],
    )
    def test_coin(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().coin(*test_args)
        assert node
        assert node.evaluate() == expected

    def test_connectedComponent(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().connectedComponent()
        assert node
        assert node.evaluate() == "g.V().connectedComponent()"

    def test_cyclicPath(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().cyclicPath()
        assert node
        assert node.evaluate() == "g.V().cyclicPath()"

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().dedup("arg")'),
            (["arg1", "arg2"], 'g.V().dedup("arg1","arg2")'),
        ],
    )
    def test_dedup(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().dedup(*test_args)
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

    def test_emit(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().emit()
        assert node
        assert node.evaluate() == "g.V().emit()"

    def test_filter(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().filter(g.V())
        assert node
        assert node.evaluate() == "g.V().filter(g.V())"

    def test_flatMap(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().flatMap(g.V())
        assert node
        assert node.evaluate() == "g.V().flatMap(g.V())"

    def test_fold(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().fold()
        assert node
        assert node.evaluate() == "g.V().fold()"

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().hasId("arg")'),
            (["arg1", "arg2"], 'g.V().hasId("arg1","arg2")'),
        ],
    )
    def test_hasId(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().hasId(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().hasKey("arg")'),
            (["arg1", "arg2"], 'g.V().hasKey("arg1","arg2")'),
        ],
    )
    def test_hasKey(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().hasKey(*test_args)
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
            (["arg"], 'g.V().hasNot("arg")'),
        ],
    )
    def test_hasNot(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().hasNot(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().hasValue("arg")'),
            (["arg1", "arg2"], 'g.V().hasValue("arg1","arg2")'),
        ],
    )
    def test_hasValue(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().hasValue(*test_args)
        assert node
        assert node.evaluate() == expected

    def test_group(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().group()
        assert node
        assert node.evaluate() == "g.V().group()"

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().groupCount()"),
            (["arg"], 'g.V().groupCount("arg")'),
        ],
    )
    def test_groupCount(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().groupCount(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().from("arg")'),
        ],
    )
    def test_from_(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().from_(*test_args)
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
            ([], "g.V().identity()"),
        ],
    )
    def test_identity(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().identity(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().in("arg")'),
            (["arg1", "arg2"], 'g.V().in("arg1","arg2")'),
        ],
    )
    def test_in_(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().in_(*test_args)
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

    def test_local(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().local(g.V())
        assert node
        assert node.evaluate() == "g.V().local(g.V())"

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
            ([], "g.V().loops()"),
            (["arg"], 'g.V().loops("arg")'),
        ],
    )
    def test_loops(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().loops(*test_args)
        assert node
        assert node.evaluate() == expected

    def test_map(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().map(g.V())
        assert node
        assert node.evaluate() == "g.V().map(g.V())"

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
            (["arg"], 'g.V().math("arg")'),
        ],
    )
    def test_math(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().math(*test_args)
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

    def test_option(self) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().option(g.V())
        assert node
        assert node.evaluate() == "g.V().option(g.V())"

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
            ([], "g.V().peerPressure()"),
        ],
    )
    def test_peerPressure(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().peerPressure(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().profile()"),
        ],
    )
    def test_profile(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().profile(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().project("arg")'),
            (["arg1", "arg2"], 'g.V().project("arg1","arg2")'),
        ],
    )
    def test_project(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().project(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().sack()"),
        ],
    )
    def test_sack(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().sack(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([1], "g.V().sample(1)"),
        ],
    )
    def test_sample(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().sample(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().shortestPath()"),
        ],
    )
    def test_shortestPath(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().shortestPath(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().simplePath()"),
        ],
    )
    def test_simplePath(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().simplePath(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([1], "g.V().skip(1)"),
        ],
    )
    def test_skip(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().skip(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg1"], 'g.V().subgraph("arg1")'),
        ],
    )
    def test_subgraph(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().subgraph(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().sum()"),
        ],
    )
    def test_sum(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().sum(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().tail()"),
        ],
    )
    def test_tail(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().tail(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([0], "g.V().timeLimit(0)"),
            ([1], "g.V().timeLimit(1)"),
        ],
    )
    def test_timeLimit(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().timeLimit(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([0], "g.V().times(0)"),
            ([1], "g.V().times(1)"),
        ],
    )
    def test_times(self, test_args: typing.List[int], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().times(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([""], 'g.V().to("")'),
            (["arg"], 'g.V().to("arg")'),
        ],
    )
    def test_to(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().to(*test_args)
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
            ([], "g.V().tree()"),
            (["arg"], 'g.V().tree("arg")'),
        ],
    )
    def test_tree(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().tree(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().unfold()"),
        ],
    )
    def test_unfold(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().unfold(*test_args)
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

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            (["arg"], 'g.V().with("arg")'),
        ],
    )
    def test_with_(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().with_(*test_args)
        assert node
        assert node.evaluate() == expected

    @pytest.mark.parametrize(
        "test_args,expected",
        [
            ([], "g.V().write()"),
        ],
    )
    def test_write(self, test_args: typing.List[str], expected: str) -> None:
        from gremlin.graph import DefaultGraphTraversal

        g = DefaultGraphTraversal()
        assert g
        node = g.V().write(*test_args)
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
