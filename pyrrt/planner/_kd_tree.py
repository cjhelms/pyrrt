import dataclasses
import typing

import scipy.spatial

import pyrrt.space.distance
import pyrrt.space.interface

_T = typing.TypeVar("_T")


class KDTree(typing.Generic[pyrrt.space.interface.T, _T]):
    def __init__(
        self,
        get_point: typing.Callable[[_T], pyrrt.space.interface.T],
        distance_function: pyrrt.space.distance.DistanceFunction[
            pyrrt.space.interface.T
        ],
    ) -> None:
        self._get_point = get_point
        self._distance_function = distance_function
        self._nodes: list[_T] = []

    def insert(self, node: _T) -> None:
        self._nodes.append(node)

    def find_nearest_neighbor(self, point: pyrrt.space.interface.T) -> _T:
        kd_tree = scipy.spatial.KDTree(
            [dataclasses.astuple(self._get_point(n)) for n in self._nodes]
        )
        _, index = kd_tree.query([dataclasses.astuple(point)])
        return self._nodes[index]

    def __len__(self) -> int:
        return len(self._nodes)
