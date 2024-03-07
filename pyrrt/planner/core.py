from __future__ import annotations

import abc
import copy
import dataclasses
import typing

import pyrrt.planner._kd_tree
import pyrrt.space.distance
import pyrrt.space.interface
import pyrrt.space.point_in_time


class Metadata(typing.Protocol):
    @classmethod
    def make_root(cls) -> typing.Self: ...


_MT = typing.TypeVar("_MT", bound=Metadata)


class CoreRRT(typing.Generic[pyrrt.space.interface.T, _MT], abc.ABC):
    def __init__(
        self,
        metadata_class: typing.Type[_MT],
        distance_function: pyrrt.space.distance.DistanceFunction[
            pyrrt.space.interface.T
        ],
    ) -> None:
        self.__metadata_class = metadata_class

        def get_point(
            node: Node[pyrrt.space.interface.T, _MT]
        ) -> pyrrt.space.interface.T:
            return node.point.point

        self.__kd_tree = pyrrt.planner._kd_tree.KDTree(get_point, distance_function)

    @typing.final
    def explore(self, initial_point: pyrrt.space.interface.T) -> None:
        if len(self.__kd_tree) > 0:
            raise self.AlreadyExploredError(
                "Must create a new RRT object to explore again!"
            )
        self.__kd_tree.insert(
            Node(
                pyrrt.space.point_in_time.PointInTime.make_with_starting_time_stamp(
                    initial_point
                ),
                self.__metadata_class.make_root(),
            )
        )
        self._explore()

    @abc.abstractmethod
    def _explore(self) -> None:
        raise NotImplementedError()

    @typing.final
    def _find_nearest_neighbor(
        self, point: pyrrt.space.interface.T
    ) -> NodeView[pyrrt.space.interface.T, _MT]:
        assert len(self.__kd_tree) > 0, "Must start exploration before searching tree!"
        return NodeView(self.__kd_tree.find_nearest_neighbor(point), self.__kd_tree)

    @typing.final
    def __len__(self) -> int:
        return len(self.__kd_tree)

    class AlreadyExploredError(Exception):
        pass


@dataclasses.dataclass
class Node(typing.Generic[pyrrt.space.interface.T, _MT]):
    point: pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T]
    metadata: _MT


class NodeView(typing.Generic[pyrrt.space.interface.T, _MT]):
    def __init__(
        self,
        node: Node[pyrrt.space.interface.T, _MT],
        kd_tree: pyrrt.planner._kd_tree.KDTree[
            pyrrt.space.interface.T, Node[pyrrt.space.interface.T, _MT]
        ],
    ) -> None:
        self._node = node
        self._kd_tree = kd_tree

    @property
    def point(
        self,
    ) -> pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T]:
        return copy.copy(self._node.point)

    @property
    def metadata(self) -> _MT:
        return copy.copy(self._node.metadata)

    def add_child(self, value: Node[pyrrt.space.interface.T, _MT]) -> None:
        self._kd_tree.insert(value)
