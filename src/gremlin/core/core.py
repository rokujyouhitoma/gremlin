from abc import ABCMeta

from gremlin.core.schema import JanusGraphManagement


class JanusGraph(metaclass=ABCMeta):
    def close(self) -> None:
        pass

    def openManagement(self) -> JanusGraphManagement:
        pass
