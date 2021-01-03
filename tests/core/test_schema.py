class TestJanusGraphManagement:
    def test_interfaces(self) -> None:
        from gremlin.core.schema import (
            JanusGraphManagement,
            JanusGraphIndex,
            PropertyKey,
            EdgeLabel,
        )

        m = JanusGraphManagement()
        assert m
        m.addIndexKey(JanusGraphIndex(), PropertyKey())
        m.buildEdgeIndex(EdgeLabel(), "")
        m.commit()
        m.printSchema()
        m.rollback()
