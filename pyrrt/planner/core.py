from __future__ import annotations

import abc
import copy
import dataclasses
import typing

import typing_extensions

from pyrrt import space

from .kd_tree import KDTree


class Metadata(typing.Protocol):
    @classmethod
    def make_root(cls) -> typing_extensions.Self: ...


_MT = typing.TypeVar("_MT", bound=Metadata)


class CoreRRT(typing.Generic[space.T, _MT], abc.ABC):
    def __init__(
        self,
        metadata_class: typing.Type[_MT],
        distance_function: space.DistanceFunction[space.T],
    ) -> None:
        self.__metadata_class = metadata_class

        def get_point(node: Node[space.T, _MT]) -> space.T:
            return node.point.point

        self.__kd_tree = KDTree(get_point, distance_function)

    @typing.final
    def explore(self, initial_point: space.T) -> None:
        if len(self.__kd_tree) > 0:
            raise self.AlreadyExploredError(
                "Must create a new RRT object to explore again!"
            )
        self.__kd_tree.insert(
            Node(
                space.PointInTime.make_with_starting_time_stamp(initial_point),
                self.__metadata_class.make_root(),
            )
        )
        self._explore()

    @abc.abstractmethod
    def _explore(self) -> None:
        raise NotImplementedError()

    @typing.final
    def _find_nearest_neighbor(self, point: space.T) -> NodeView[space.T, _MT]:
        assert len(self.__kd_tree) > 0, "Must start exploration before searching tree!"
        return NodeView(self.__kd_tree.find_nearest_neighbor(point), self.__kd_tree)

    @typing.final
    def __len__(self) -> int:
        return len(self.__kd_tree)

    class AlreadyExploredError(Exception):
        pass


@dataclasses.dataclass
class Node(typing.Generic[space.T, _MT]):
    point: space.PointInTime[space.T]
    metadata: _MT


class NodeView(typing.Generic[space.T, _MT]):
    def __init__(
        self, node: Node[space.T, _MT], kd_tree: KDTree[space.T, Node[space.T, _MT]]
    ) -> None:
        self._node = node
        self._kd_tree = kd_tree

    @property
    def point(self) -> space.PointInTime[space.T]:
        return copy.copy(self._node.point)

    @property
    def metadata(self) -> _MT:
        return copy.copy(self._node.metadata)

    def add_child(self, value: Node[space.T, _MT]) -> None:
        self._kd_tree.insert(value)
