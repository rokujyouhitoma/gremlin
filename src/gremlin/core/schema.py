from abc import ABCMeta


class JanusGraphIndex:
    pass


class PropertyKey:
    pass


class RelationTypeIndex:
    pass


class EdgeLabel:
    pass


class JanusGraphManagement(metaclass=ABCMeta):
    def addIndexKey(self, index: JanusGraphIndex, key: PropertyKey) -> None:
        pass

    def buildEdgeIndex(self, label: EdgeLabel, name: str) -> RelationTypeIndex:
        pass

    def commit(self) -> None:
        pass

    def printSchema(self) -> str:
        pass

    def rollback(self) -> None:
        pass
