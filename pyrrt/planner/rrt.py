from __future__ import annotations

import typing

import pyrrt.planner.core
import pyrrt.region.interface
import pyrrt.space.distance
import pyrrt.space.interface
import pyrrt.steer.interface


class _Metadata:
    @classmethod
    def make_root(cls) -> _Metadata:
        return _Metadata()


class RRT(pyrrt.planner.core.CoreRRT[pyrrt.space.interface.T, _Metadata]):
    def __init__(
        self,
        space_class: typing.Type[pyrrt.space.interface.T],
        distance_function: pyrrt.space.distance.DistanceFunction[
            pyrrt.space.interface.T
        ],
        steer_function: pyrrt.steer.interface.SteerFunction[pyrrt.space.interface.T],
        free_space: pyrrt.region.interface.IRegion[pyrrt.space.interface.T],
        stop_criteria: StopCriteria,
    ) -> None:
        super().__init__(_Metadata, distance_function)
        self._space_class = space_class
        self._distance_function = distance_function
        self._steer_function = steer_function
        self._free_space = free_space
        self._stop_criteria = stop_criteria

    @typing.override
    def _explore(self) -> None:
        while not self._stop_criteria(len(self)):
            self._maybe_extend_tree()

    def _maybe_extend_tree(self) -> None:
        random_point = self._free_space.draw_sample()
        nearest_node = self._find_nearest_neighbor(random_point)
        new_point = self._steer_function(nearest_node.point, random_point)
        if new_point in self._free_space:
            nearest_node.add_child(pyrrt.planner.core.Node(new_point, _Metadata()))


class StopCriteria(typing.Protocol):
    def __call__(self, node_count: int) -> bool: ...
