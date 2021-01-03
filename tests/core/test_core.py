class TestJanusGraph:
    def test_interfaces(self) -> None:
        from gremlin.core.core import JanusGraph

        j = JanusGraph()
        assert j
        j.close()
        j.openManagement()
